from pymongo import MongoClient


class LabirintPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.books

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)

        return item
