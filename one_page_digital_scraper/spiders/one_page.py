import scrapy
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from one_page_digital_scraper.items import OnePageDigitalScraperItem
import pandas as pd

class one_page_scrape(CrawlSpider):
    links_viewed = []
    # Below is the name of the scraper, I think this is what you will call
    # from the terminal.
    name = 'one_page_scraper'
    # This will ensure that the scrape stays within the domains listed below.
    allowed_domains = ['digital.nhs.uk']
    # This list is all the URLs you want to start from.
    urls_df = pd.read_csv('google_analytics_missing_from_scrape.csv')
    urls_df['complete_urls'] = 'https://www.digital.nhs.uk'+urls_df['Page']
    start_urls = list(urls_df['complete_urls'])
    # start_urls = ['https://www.digital.nhs.uk/']

    def parse(self, response):
        items = []
        item = OnePageDigitalScraperItem()
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
