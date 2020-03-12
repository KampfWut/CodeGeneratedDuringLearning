# -*- coding: utf-8 -*-
import scrapy, re
from WeatherProject_08.items import Weatherproject08Item

class DalianspiderSpider(scrapy.Spider):
    name = 'daLianSpider'
    allowed_domains = ['www.tianqi.com']
    start_urls = []
    citys = ["dalian", "shenyang", "fushun"]
    for city in citys:
        start_urls.append("http://www.tianqi.com/" + city + "/")

    def parse(self, response):
        print(">>>"*20)
        item = Weatherproject08Item()
        
        item['cityData'] = response.xpath('//dd[@class="name"]/h2//text()').extract()
        item['week'] = response.xpath('//ul[@class="week"]/li/b//text()').extract()
        item['img'] = response.xpath('//ul[@class="week"]/li/img/@src').extract()

        tempUp = response.xpath('//ul/li/span//text()').extract()
        tempDown = response.xpath('//ul/li/b//text()').extract()
        temperUpLimited = []
        temperDownLimited = []
        for i in tempUp:
            if re.match("[0-9]*", i).group() == i:
                temperUpLimited.append(i)
        for i in tempDown:
            if re.match("[0-9]*", i).group() == i:
                temperDownLimited.append(i)
        temper = []
        for i in range(len(temperUpLimited)):
            temper.append(temperDownLimited[i] + " - " + temperUpLimited[i])
        item['temperature'] = temper

        item['weather'] = response.xpath('//ul[@class="txt txt2"]/li//text()').extract()
        item['wind'] = response.xpath('//ul[@class="txt"]/li//text()').extract()

        return item
            





