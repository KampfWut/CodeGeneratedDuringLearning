# -*- coding: utf-8 -*-
import scrapy
from MovieProject_07.items import Movieproject07Item

class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['dytt8.net']
    start_urls = []
    for i in range(1, 180):
        start_urls.append('http://www.dytt8.net/html/gndy/dyzz/list_23_' + str(i) + '.html')

    def parse(self, response):
        subSelector = response.xpath('//td[@colspan="2" and @style="padding-left:3px"]')

        items = []
        for sub in subSelector:
            item = Movieproject07Item()
            item['movieName'] = sub.xpath("./text()").extract()
            items.append(item)

        return items
