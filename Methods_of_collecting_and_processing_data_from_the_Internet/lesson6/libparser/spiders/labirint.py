import scrapy
from scrapy.http import HtmlResponse
from libparser.items import LibparserItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = [
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&id_genre=2498&display=table&order=popularity&way=forward',
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&display=table&order=popularity&way=forward&id_genre=2556',
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&display=table&order=popularity&way=forward&id_genre=2794',
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&display=table&order=popularity&way=forward&id_genre=2793',
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&display=table&order=popularity&way=forward&id_genre=2791',
        'https://www.labirint.ru/books/?nrd=1&available=1&paperbooks=1&ebooks=1&display=table&order=popularity&way=forward&id_genre=2792']

    def parse(self, response: HtmlResponse):
        next_page = 'https://www.labirint.ru/books/' + response.xpath(
            "//div[@class='pagination-next']//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//tbody[@class='products-table__body']/tr//td[1]/div/a/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)

    def book_parse(self, response: HtmlResponse):
        name = response.xpath("//div[@id='product-title']/h1/text()").get()
        author = response.xpath("//div[@class='product-description']/div[2]/a/text()").get()
        temp = response.xpath("//span[@class='buying-price-val-number']/text()").get()
        if temp is None:
            price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").get()
            old_price = response.xpath("//span[@class='buying-priceold-val-number']/text()").get()
        else:
            price = temp
            old_price = None
        currency = response.xpath("//span[@class='buying-pricenew-val-currency']/text()").get()
        rate = response.xpath("//div[@id='rate']/text()").get()
        genre = response.xpath("//div[@class='genre']/a/text()").getall()
        url = response.url
        yield LibparserItem(name=name, author=author, price=price, old_price=old_price, currency=currency, rate=rate,
                            genre=genre, url=url)
