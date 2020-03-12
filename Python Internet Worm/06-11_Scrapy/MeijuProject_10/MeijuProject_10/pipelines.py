# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Meijuproject10Pipeline(object):
    def process_item(self, item, spider):
        fileName = "10_meiju100.txt"

        f = open(fileName, "a")
        f.write("{}\t".format(item["name"][0].strip()))
        if item["status"]:
            f.write("{}\t".format(item["status"][0].strip()))
        else:
            f.write("None\t")
        f.write("{}\t".format(item["typ"][0].strip()))
        f.write("{}\t".format(item["tvStation"][0].strip()))
        f.write("{}\t".format(item["upDateTime"][0].strip()))
        f.write("\n")
        f.close()

        return item
