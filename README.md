# digital_scraping

Data Science work.

## Instructions for use

This python code uses the python library scrapy, docs are here - [https://doc.scrapy.org/en/latest/](https://doc.scrapy.org/en/latest/)  

To run the scraping algorithm, navigate to ../digital_scraper and run the following command. This will save the data to the csv `csv_name.csv`.  

    $ scrapy crawl digital_scraper -o csv_name.csv -t csv  

To change the algorithm the two files you will 'need' to change are `digital.py` and `items.py`. The code has certain bits commented out simply because I wanted to use them later. There is a massive bunch of functionality that I haven't used yet, but this does what I needed it to do to get the relevant information.

