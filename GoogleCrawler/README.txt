Google Crawler (Python 2.7)

This is a basic tool to crawls google for user-inputted search terms. It saves the first 20 results returned, visits each of the result pages and stores the title, main text and meta description in MySQL database. User can also retrieve the stored information from a file directly instead of query MySQL database.

Author: Hongchen
===============================================================
METHODS:

1. This tool crawls google with the Google API. This free API allows me to return up to 4 results in a single call. To get the first 20 results, I called 4 times.

2. Use urllib to retrieve the url.

3. Apply python-goose to extract the title, main text and meta description of each result page. Goose can also be useful in video and image extraction. In this project, I only extracted the main text from the html page.

4. Store the information extracted in MySQL database.

Note: Scrapy and rq are very useful tools for speeding up the large scale html pages crawling process. However, with regard to only 20 results returned, it's not necessary to implemetn scrapy and rq here.

===============================================================
SOFTWARE TOOLS:

(1) Python 2.7.10
(2) python-goose (for installation details:  https://github.com/grangier/python-goose)
(3) MySQL (downloaded from the official website)

===============================================================
SOURCE CODE FILES:

(1) google.py
Given the inputted search terms, crawl google, return the first 20 results and save the useful information of each result page to the "result.dat" file.

(2)load.sql
Create a table and load information from "results.dat" to the table in the database.

===============================================================
Here is an example usage of Google Crawler:

(1) Enter key words "love story taylor", and crawl google :
$ python google.py love story taylor

The useful information for the first 20 results will be stored in the "result.dat" file. Users can access to it by opening the file in any editor such as sublime.

(2) To store the information in the database, select a database in mysql, and then:

mysql > source load.sql

Users can see the table by:
mysql > SELECT * FROM GoogleCrawler;

Each record will be like:

|    1 | TAYLOR SWIFT LYRICS - Love Story                                  | http://www.azlyrics.com/lyrics/taylorswift/lovestory.html               | We were both young when I first saw you.

 I close my eyes and the flashback starts:

 I'm standing there on a balcony in summer air.....(lyrics)

 =============================================================
 TODO:

 Video and image extraciton





 