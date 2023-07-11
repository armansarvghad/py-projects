import scrapy

class MySpider(scrapy.Spider):
    name = 'my_crawler'
    start_urls = ['https://example.com']

    def parse(self, response):
        # Extract data from the response using XPath or CSS selectors
        # Example: extracting all links on the page
        links = response.xpath('//a/@href').getall()
        for link in links:
            yield {
                'url': link
            }

        # Follow links to other pages for further crawling
        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)

# Run the crawler
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'LOG_ENABLED': False  # Disable logging for cleaner output
})

process.crawl(MySpider)
process.start()
