import os.path
from pprint import pprint

import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse


class LeruaParserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.shop

    def process_item(self, item, spider):
        pprint(item)
        collection = self.db[spider.name]
        collection.save(item)
        return item


class LeruaPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

