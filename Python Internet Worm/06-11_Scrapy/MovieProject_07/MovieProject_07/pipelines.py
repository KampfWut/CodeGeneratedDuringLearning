# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class Movieproject07Pipeline(object):
    def process_item(self, item, spider):
        now = time.strftime("%Y-%m-%d", time.localtime())
        fileName = '07_movie_'+ now + '.txt'

        f = open(fileName, 'a')
        f.write(item['movieName'][0] + "\n")
        f.close()
        
        return item
