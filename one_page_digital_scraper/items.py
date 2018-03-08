# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OnePageDigitalScraperItem(scrapy.Item):
    # html = scrapy.Field()
    # redirect_urls = scrapy.Field()
    # request_url = scrapy.Field()
    response_url = scrapy.Field()
    title = scrapy.Field()
    paragraphs = scrapy.Field()
    links = scrapy.Field()
    header1 = scrapy.Field()
    header2 = scrapy.Field()
    header3 = scrapy.Field()
    # children = scrapy.Field()
    template = scrapy.Field()
    paragraph_pubs = scrapy.Field()
