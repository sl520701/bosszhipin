# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem
import time
import random
class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=[1-2]'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/.+~'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        job = response.xpath('//div[@class="name"]/h1/text()').get()
        salary = response.xpath('//div[@class="name"]/span/text()').get()
        welfare = response.xpath('//div[@class="job-tags"][1]/span/text()').getall()
        i = len(welfare)
        i = (int(i) / 2)
        welfares = welfare[0:int(i)]
        era = response.xpath('//div[@class="info-primary"]/p[1]/text()')[0].get()
        year = response.xpath('//div[@class="info-primary"]/p[1]/text()')[1].get()
        education = response.xpath('//div[@class="info-primary"]/p[1]/text()')[2].get()
        descripe = response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').getall()
        descripes = []
        for each in descripe:
            each = each.strip()
            descripes.append(each)
        introduction = response.xpath('//div[@class="job-sec company-info"]/div[@class="text"]/text()').getall()
        introductions = []
        for each in introduction:
            each = each.strip()
            introductions.append(each)
        item = BossItem(job = job,salary=salary,welfares=welfares,era=era,year=year,education=education,descripes = descripes,introductions=introductions)
        time.sleep(random.randint(1,6))
        yield item

        # # print(1)
        # time.sleep(2)
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

