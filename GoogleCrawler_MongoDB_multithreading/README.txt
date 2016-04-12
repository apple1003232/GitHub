Google Crawler (Python 2.7)

This is a basic tool to crawls google for user-inputted search terms with multithreading. It saves the first 20 results returned, visits each of the result pages and stores the title, main text, meta description and main image in Mongodb database. 

Author: Hongchen
===============================================================
METHODS:

1. This tool crawls google with the Google API. This free API allows me to return up to 4 results in a single call. To get the first 20 results, I called 4 times. 20 results are stored in a queue.

2. Create 13 threads. For each thread, get one result from the queue, and apply python-goose to extract the title, main text, meta description and top image of each result page. Goose can also be useful in video and image extraction. In this project, I only extracted the main text and the top image sourcefrom the html page.

3. Store the information extracted in Mongodb database.

Note: Since only 20 results are required to return, 

===============================================================
SOFTWARE TOOLS:

(1) Python 2.7.10
(2) python-goose (for installation details:  https://github.com/grangier/python-goose)
(3) Mongodb (for installation details: https://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/)
(4) Robomongo (optional)

===============================================================
SOURCE CODE FILES:

(1) google.py
Given the inputted search terms, crawl google, return the first 20 results and store the useful information of each result page to Mongodb in multithreadings.

===============================================================
Here is an example usage of Google Crawler:

(1) Enter key words "python", and crawl google :
$ python google.py python

The useful information for the first 20 results will be stored in the MongoDB. You can used Robomongo to view the data in the database if you like.

 =============================================================
 TODO:

 Video extraciton





 