# pillow installed
# 1) Взять любую категорию товаров на сайте Леруа Мерлен. Собрать следующие данные:
# ● название;
# ● все фото;
# ● ссылка;
# ● цена.
#
# Реализуйте очистку и преобразование данных с помощью ItemLoader. Цены должны быть в виде числового значения.
#
# Дополнительно:
# 2)Написать универсальный обработчик характеристик товаров,
# который будет формировать данные вне зависимости от их типа и количества.

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
