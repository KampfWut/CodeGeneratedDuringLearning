# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Getproxyproject09Pipeline(object):
    def process_item(self, item, spider):
        fileName = "09_proxy.txt"

        f1 = open(fileName, "a")
        f1.write("{:s}\t".format(item["ip"][0].strip()))
        f1.write("{:s}\t".format(item["port"][0].strip()))
        f1.write("{:s}\t".format(item["location"][0].strip()))
        f1.write("{:s}\t".format(item["iptype"][0].strip()))
        f1.write("{:s}\t".format(item["protocol"][0].strip()))
        f1.write("{:s}\t".format(item["alivetime"][0].strip()))
        f1.write("{:s}\t".format(item["checktime"][0].strip()))
        f1.write("\n")
        f1.close()

        f2 = open("use_proxy.txt", "a")
        f2.write("\"{}:{}:{}\",\n".format(item["ip"][0].strip(), item["port"][0].strip(), item["protocol"][0].strip().lower()))
        f2.close()

        return item
