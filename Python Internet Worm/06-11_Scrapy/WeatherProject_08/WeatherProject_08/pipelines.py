# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os.path
import time
import json
import codecs
import urllib.request


class Weatherproject08Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime("%Y%m%d", time.localtime())
        fileName = "08_Weather_" + today + ".txt"

        f1 = open(fileName, 'a')
        f1.write("City :" + item["cityData"][0] + "\n")
        f1.write("-" * 60 + "\n")
        for i in range(len(item["week"])):
            f1.write("{:<12}".format(item["week"][i]))
            f1.write("{:<12}".format(item["temperature"][i]))
            f1.write("{:<8}".format(item["weather"][i]))
            f1.write("{:<8}".format(item["wind"][i]))
            temp = item["img"][i].split("/")
            f1.write("{:<12}".format(temp[-1]))
            f1.write("\n")
        f1.write("-" * 60 + "\n")
        f1.close()

        fileName = "08_Weather_" + today + ".json"
        f2 = codecs.open(fileName, 'a', encoding = "utf-8")
        line = json.dumps(dict(item), ensure_ascii = False) + "\n"
        f2.write(line)
        f2.close()

        return item
