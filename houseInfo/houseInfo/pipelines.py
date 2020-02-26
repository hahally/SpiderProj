# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class HouseinfoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = 'loupan'

    # 最先执行
    @classmethod
    def from_crawler(cls, crawler):
        print("------------ from_crawler --------------")

        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    # 在 from_crawler 之后执行
    def open_spider(self, spider):
        print("------------ open_spider --------------")
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]


    # 在 open_spider 以及 parse 之后执行
    def process_item(self, item, spider):
        print("----- process_item -----" )
        name = self.collection_name
        self.db[name].insert(dict(item))

        return item

    # 在 process_item 之后执行
    def close_spider(self, spider):
        print("------------ close_spider --------------")
        self.client.close()

