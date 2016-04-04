
import urllib
import json
from goose import Goose
import sys

def GoogleSearch(argu):
	url2 = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&start="

	q = "&q="
	keyWords = argu #"love story taylor"
	startNums = ["0","4","8","12","16"]

	searchResults = []

	for num in startNums:
		theUrl = url2 + num + q + keyWords
		f = urllib.urlopen(theUrl)
		j = json.load(f)
		searchResults += j["responseData"]["results"]

	Id = 1
	g = Goose()
	with open("result.dat", "w") as of:
		for obj in searchResults:
			# print obj["unescapedUrl"]
			resultUrl = obj["unescapedUrl"]
			# print resultUrl
			article = g.extract(url = resultUrl)
			# print article.title
			line = article.title + "|*|" + resultUrl + "|*|" + article.cleaned_text[:4000]
			of.write(str(Id) + "|*|")
			of.write(line.encode('utf-8') + "|**|")
			Id += 1
	return

line = ""
for ele in sys.argv[1:]:
	line += " " + ele

GoogleSearch(line)
	
