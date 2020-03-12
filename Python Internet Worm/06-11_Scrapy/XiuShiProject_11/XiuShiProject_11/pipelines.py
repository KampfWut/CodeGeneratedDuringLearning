# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Xiushiproject11Pipeline(object):
    def process_item(self, item, spider):
        fileName = "11_xiushi.txt"

        f = open(fileName, "a")
        f.write("{}\n".format(item["author"][0].strip()))
        f.write("{}\n".format(item["content"][0].strip()))
        f.write("{}\n".format(item["funNum"][0].strip()))
        f.write("{}\n".format(item["talkNum"][0].strip()))
        f.write("\n")
        f.close()

        return item