# Python 3.6.5

import urllib.request
import re
import time
from bs4 import BeautifulSoup
from myLog import myLog as mylog


class item(object):
    bookTypeA = None
    bookTypeB = None
    bookName = None
    wordsNum = None
    authorName = None
    content = None

class getTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 10
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    # get all Url will be use 
    def getUrls(self, pageSum):
        urls = []
        pns = range(1, pageSum)
        ul = self.url.split("=")
        for pn in pns:
            ul[-1] = str(pn)
            url = "=".join(ul)
            urls.append(url)
        self.log.info("> Get the Urls success.")
        return urls

    # spider web
    def spider(self, urls):
        self.log.info("> Start Spider.")
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'html.parser')
            tagsli = soup.find_all('div', attrs = {"class":"book-mid-info"})
            for tag in tagsli:
                i = item()

                tagA = tag.find('p', attrs = {"class":"author"}).find_all('a')
                i.bookTypeA = tagA[1].get_text()
                i.bookTypeB = tagA[2].get_text()
                i.bookName = tag.find('h4').a.get_text()

                temp = tag.find('p', attrs = {"class":"update"}).span.span.get_text()
                i.wordsNum = temp

                i.authorName = tagA[0].get_text()
                i.content = tag.find('p', attrs = {"class":"intro"}).get_text().strip()
                
                items.append(i)
                self.log.info("> Get the item with name \"{}\" Success.".format(i.bookName))
        return items
    
    # save as file
    def pipelines(self, items):
        self.log.info("> Start Pipelines.")
        fileName = "15_QiDianBook.txt"
        f = open(fileName, 'w')
        for i in items:
            f.write("-" * 80)
            f.write("\nName: {}\t author: {}\t Type: {}-{}\n".format(i.bookName, i.authorName, i.bookTypeA, i.bookTypeB))
            f.write("content:\n{}\n".format(i.content))
            f.write("Words number: {}\n\n".format(i.wordsNum))
            self.log.info("> Save \"{}\" in to file Success.".format(i.bookName))
        f.close()

    # back url
    def getResponseContent(self, url):
        try:
            Res = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"})
            res = urllib.request.urlopen(Res)
        except:
            self.log.error("> Back url Fail!")
        else:
            self.log.info("> Back url Success, Url is \"{}\".".format(url))
            message = res.read().decode("utf-8")
            '''
            # 删除注释， 防止soup读不到
            delstr = ["-->", "<!--"]
            for string in delstr:
                message = message.replace(string,"")
            '''
            return message

if __name__ == "__main__":
    # url不要使用utf-8格式的， 会失败
    url = "https://www.qidian.com/all?action=1&orderId=&page=1"
    GTI = getTiebaInfo(url)
        


