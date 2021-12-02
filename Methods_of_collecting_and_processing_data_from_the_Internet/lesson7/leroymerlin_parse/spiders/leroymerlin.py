import scrapy
from scrapy.http import HtmlResponse
from leroymerlin_parse.items import LeroymerlinParseItem
from scrapy.loader import ItemLoader


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, query):
        super().__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={query}']

    def parse(self, response: HtmlResponse):
        new_page = response.xpath("//a[@data-qa-pagination-item='right']/@href").get()
        if new_page:
            new_page = 'https://leroymerlin.ru' + new_page
            yield response.follow(new_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='product-name']")
        for link in links:
            yield response.follow(link, callback=self.leroymerlin_item_parse)

    def leroymerlin_item_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroymerlinParseItem(), response=response)
        loader.add_xpath('name', "//h1[@class='header-2']/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('photos', "//img[@slot='thumbs']/@src")
        loader.add_xpath('feature_names', "//dt[@class='def-list__term']/text()")
        loader.add_xpath('feature_values', "//dd[@class='def-list__definition']/text()")
        loader.add_value('url', response.url)
        yield loader.load_item()
