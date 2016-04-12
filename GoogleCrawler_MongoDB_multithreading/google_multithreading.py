import urllib
import json
import sys
import Queue
import threading
import time

from goose import Goose
from pymongo import MongoClient

exitFlag = 0


class  myThread(threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q

	def run(self):
		print "Starting " + self.name
		process_data(self.name, self.q)
		print "Exiting " + self.name

def process_data(threadName, q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			global Id
			print "%s processing No.%s result page..." % (threadName, Id)
			data = q.get()
			g = Goose()
			resultUrl = data["unescapedUrl"]
			article = g.extract(url = resultUrl)
			item = {}
			item['title'] = data["titleNoFormatting"]
			item['url'] = resultUrl
			item['keyWords'] = keyWords
			item['description'] = article.cleaned_text[:4000]
			if article.top_image:
				item['image'] = article.top_image.src
			else:
				item['image'] = ""
			insert(item)
			Id += 1
			
			queueLock.release()
			
			
		else:
			queueLock.release()
		time.sleep(1)


def insert(item):
	# connect to MongoDB 
	client = MongoClient('localhost', 27017)
	db = client['google']
	collection = db['results']
	if collection.find({'url': item['url']}).count() == 0:
		collection.insert_one(item)

def GoogleSearch(argu):
	url2 = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&start="

	q = "&q="
	keyWords = argu #"python"
	startNums = ["0","4","8","12","16"]

	
	print "Start to crawl Google with keyWords: %s" % keyWords

	# store 20 results in a Queue
	for num in startNums:
		theUrl = url2 + num + q + keyWords
		f = urllib.urlopen(theUrl)
		j = json.load(f)
		for res in j["responseData"]["results"]:
			workQueue.put(res)

	
##########################################################
start_time = time.clock()
keyWords = ""
for ele in sys.argv[1:]:
	keyWords += " " + ele


threadList = []
for i in range(13):
	threadList.append("Thread-" + str(i+1))

queueLock = threading.Lock()
workQueue = Queue.Queue(20)
threads = []
threadID = 1
Id = 1

for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1

queueLock.acquire()
GoogleSearch(keyWords)
queueLock.release()


while not workQueue.empty():
	pass

exitFlag = 1

for t in threads:
	t.join()
print "Exiting Main Thread"
print "-----End-----"
end_time = time.clock()
print end_time - start_time

