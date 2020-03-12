# -*- coding: utf-8 -*-
import scrapy
from GetProxyProject_09.items import Getproxyproject09Item

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['www.xicidaili.com']
    start_urls = []
    ipt = ["nn/", "nt/"]
    for item in ipt:
        for i in range(1, 5):
            start_urls.append('http://www.xicidaili.com/' + item + str(i))

    def parse(self, response):
        subSelector = response.xpath('//tr')
        items = []
        for sub in subSelector:
            item = Getproxyproject09Item()
            item["ip"] = sub.xpath('.//td[2]//text()').extract()
            item["port"] = sub.xpath('.//td[3]//text()').extract()
            if sub.xpath('.//td[4]/a//text()'):
                item["location"] = sub.xpath('.//td[4]/a//text()').extract()
            else:
                item["location"] = sub.xpath('.//td[4]//text()').extract()
            item["iptype"] = sub.xpath('.//td[5]//text()').extract()
            item["protocol"] = sub.xpath('.//td[6]//text()').extract()
            item["alivetime"] = sub.xpath('.//td[9]//text()').extract()
            item["checktime"] = sub.xpath('.//td[10]//text()').extract()
            items.append(item)
        return items

