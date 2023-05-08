import scrapy


class LabirintItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()
    author = scrapy.Field()
