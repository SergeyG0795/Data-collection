import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def clear_price(value):
    value = value.replace('\xa0', '')
    try:
        return int(value)
    except:
        return value


class LeruaParserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clear_price))
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clear_price))
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
