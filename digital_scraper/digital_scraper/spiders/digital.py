# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from digital_scraper.items import DigitalScraperItem


class DigitalSpider(CrawlSpider):
    links_viewed = []
    # Below is the name of the scraper, I think this is what you will call
    # from the terminal.
    name = 'digital_scraper'
    # This will ensure that the scrape stays within the domains listed below.
    allowed_domains = ['digital.nhs.uk']
    # This list is all the URLs you want to start from.
    start_urls = ['https://www.digital.nhs.uk/article/196/Systems-and-services',
                  'https://www.digital.nhs.uk/', 'https://www.content.digital.nhs.uk',
                  'https://www.digital.nhs.uk/news-and-events']

    # This spider has one rule: extract all (unique and canonicalized) links,
    # process the links with the method 'process_links', follow the
    # resulting links and parse them using the 'parse_items' method.

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=False,
                unique=True
            ),
            follow=True,
            callback="parse_items",
            process_links = "process_links"
        )
    ]

    # This is a method which starts the requests by visiting all URLs
    # specified in start_urls.

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_items, dont_filter=True)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # This function processes the links before visiting and parsing them. It
    # ensures that no link is visited twice and that the scraping avoids the
    # search pages on the digital website. I used it to stop it from visiting
    # certain search pages.

    def process_links(self, links):
        for link in links:
            if 'mv' in link.url:
                continue
            elif '//content.digital.nhs.uk' in link.url:
                continue
            elif '//digital.nhs.uk' in link.url:
                continue
            elif 'http://content.digital.nhs.uk/article/2021/Website-Search' in link.url:
                continue
            elif 'http://www.content.digital.nhs.uk/article/2021/Website-Search' in link.url:
                continue
            elif link.url in self.links_viewed:
                continue
            yield link



    # Method for parsing items. I used xpath to extract the parts I wanted. If
    # you just want the html use response.text. I append the response url to
    # self.links_viewed to ensure no link is parsed twice. The returned items
    # are added to the item class in the file items.py.

    def parse_items(self, response):
        items = []
        self.links_viewed.append(response.url)
        item = DigitalScraperItem()
        # item['html'] = response.text
        # item['redirect_urls'] = response.meta.get('redirect_urls',[response.url])
        # item['request_url'] = response.meta.get('redirect_urls',[response.url])
        item['response_url'] = response.url
        item['title'] = response.xpath('//title//text()').extract()
        item['paragraphs'] = response.xpath('//p/text()').extract()
        item['links'] = response.xpath('//a//text()').extract()
        item['header1'] = response.xpath('//h1//text()').extract()
        item['header2'] = response.xpath('//h2//text()').extract()
        item['header3'] = response.xpath('//h3//text()').extract()
        # item['children'] = response.xpath('//div[@class="item article"]').extract()
        item['template'] = response.xpath('//body/@data-template').extract()
        item['paragraph_pubs'] = response.xpath('//div[contains(@class,"textblock-default")]').extract()
        items.append(item)
        # Return all the found items
        return items
