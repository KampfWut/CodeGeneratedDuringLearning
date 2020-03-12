# -*- coding: utf-8 -*-
import scrapy
from XiuShiProject_11.items import Xiushiproject11Item

class XiushispiderSpider(scrapy.Spider):
    name = 'xiushiSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        subSeclector = response.xpath('//div[@class="article block untagged mb15 typs_long"]')
        items = []
        for sub in subSeclector:
            item = Xiushiproject11Item()
            item["author"] = sub.xpath('./div[@class="author clearfix"]/a/h2//text()').extract()
            item["content"] = sub.xpath('./a/div[@class="content"]/span//text()').extract()
            item["funNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i//text()').extract()
            item["talkNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i//text()').extract()
            items.append(item)
        subSeclector = response.xpath('//div[@class="article block untagged mb15 typs_hot"]')
        for sub in subSeclector:
            item = Xiushiproject11Item()
            item["author"] = sub.xpath('./div[@class="author clearfix"]/a/h2//text()').extract()
            item["content"] = sub.xpath('./a/div[@class="content"]/span//text()').extract()
            item["funNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i//text()').extract()
            item["talkNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i//text()').extract()
            items.append(item)
        subSeclector = response.xpath('//div[@class="article block untagged mb15 typs_recent"]')
        for sub in subSeclector:
            item = Xiushiproject11Item()
            item["author"] = sub.xpath('./div[@class="author clearfix"]/a/h2//text()').extract()
            item["content"] = sub.xpath('./a/div[@class="content"]/span//text()').extract()
            item["funNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i//text()').extract()
            item["talkNum"] = sub.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i//text()').extract()
            items.append(item)
        return items
        
