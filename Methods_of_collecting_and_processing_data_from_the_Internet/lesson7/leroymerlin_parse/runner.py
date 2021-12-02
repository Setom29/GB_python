# pillow installed
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leroymerlin_parse import settings
from leroymerlin_parse.spiders.leroymerlin import LeroymerlinSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    query = 'стеллаж'
    process.crawl(LeroymerlinSpider, query=query)

    process.start()

