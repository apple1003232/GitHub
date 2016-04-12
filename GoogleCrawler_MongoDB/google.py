import urllib
import json
from goose import Goose
import sys
from pymongo import MongoClient

def GoogleSearch(argu):
	url2 = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&start="

	q = "&q="
	keyWords = argu #"love story taylor"
	startNums = ["0","4","8","12","16"]

	searchResults = []
	print "Start to crawl Google with keyWords: %s" % keyWords

	# store 20 results in searchResults
	for num in startNums:
		theUrl = url2 + num + q + keyWords
		f = urllib.urlopen(theUrl)
		j = json.load(f)
		searchResults += j["responseData"]["results"]

	# connect to MongoDB 
	client = MongoClient('localhost', 27017)
	db = client['google']
	collection = db['results']

	# extract data using Goose
	Id = 1
	g = Goose()
	
	# with open("result.dat", "w") as of:
	for obj in searchResults:
		print "Extracting No.%d result page..." % Id
		# print obj["unescapedUrl"]
		resultUrl = obj["unescapedUrl"]
		# print resultUrl
		article = g.extract(url = resultUrl)
		# print article.title
		item = {}
		# item['resultId'] = Id
		item['title'] = obj["titleNoFormatting"]
		item['url'] = resultUrl
		item['keyWords'] = keyWords
		item['description'] = article.cleaned_text[:4000]
		if collection.find({'url': item['url']}).count() == 0:
			collection.insert_one(item)
		# line = article.title + "|*|" + resultUrl + "|*|" + article.cleaned_text[:4000]
		# of.write(str(Id) + "|*|")
		# of.write(line.encode('utf-8') + "|**|")
		Id += 1
	print "-----End-----"
	return

line = ""
for ele in sys.argv[1:]:
	line += " " + ele

GoogleSearch(line)
	
