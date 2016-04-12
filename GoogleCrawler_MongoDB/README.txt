Google Crawler (Python 2.7)

This is a basic tool to crawls google for user-inputted search terms. It saves the first 20 results returned, visits each of the result pages and stores the title, main text and meta description in MySQL database. User can also retrieve the stored information from a file directly instead of query MySQL database.

Author: Hongchen
===============================================================
METHODS:

1. This tool crawls google with the Google API. This free API allows me to return up to 4 results in a single call. To get the first 20 results, I called 4 times.

2. Use urllib to retrieve the url.

3. Apply python-goose to extract the title, main text and meta description of each result page. Goose can also be useful in video and image extraction. In this project, I only extracted the main text from the html page.

4. Store the information extracted in Mongodb database.

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
Given the inputted search terms, crawl google, return the first 20 results and save the useful information of each result page to Mongodb.

===============================================================
Here is an example usage of Google Crawler:

(1) Enter key words "python", and crawl google :
$ python google.py python

The useful information for the first 20 results will be stored in the MongoDB. You can used Robomongo to view the data in the database if you like.

 =============================================================
 TODO:

 Video and image extraciton





 