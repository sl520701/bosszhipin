# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class BossPipeline(object):
    def process_item(self, item, spider):
        return item
class MongoPipline(object):
    def __init__(self,mongo_address,mongo_name):
        self.mongo_address = mongo_address
        self.mongo_name = mongo_name
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_address=crawler.settings.get('MONGO_ADDRESS'),
            mongo_name=crawler.settings.get('MONGO_NAME')
        )
    #用于获取setting中对MONGO_ADDRESS和NAME的配置制定mongpdb需要连接的地址和数据库名称
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_address)#连接mongodb
        self.db = self.client[self.mongo_name]
    def process_item(self,item,spider):
        collection = self.db['students']
        collection.insert(dict(item))
        return item#插入数据操作
    def close_spider(self,spider):
        self.client.close()
