# -*- coding: utf-8 -*-
import scrapy
from MeijuProject_10.items import Meijuproject10Item

class MoviespiderSpider(scrapy.Spider):
    name = 'movieSpider'
    allowed_domains = ['www.meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        subSelector = response.xpath('//li/div[@class="lasted-num fn-left"]')
        items = []
        for sub in subSelector:
            item = Meijuproject10Item()
            item["name"] = sub.xpath('../h5/a/text()').extract()
            item["status"] = sub.xpath('../span[@class="state1 new100state1"]/font/text()').extract()
            item["typ"] = sub.xpath('../span[@class="mjjq"]/text()').extract()
            item["tvStation"] = sub.xpath('../span[@class="mjtv"]/text()').extract()
            if sub.xpath('../div[@class="lasted-time new100time fn-right"]/text()').extract():
                item["upDateTime"] = sub.xpath('../div[@class="lasted-time new100time fn-right"]/text()').extract()
            else:
                item["upDateTime"] = sub.xpath('../div[@class="lasted-time new100time fn-right"]/font/text()').extract()
            items.append(item)

        return items


