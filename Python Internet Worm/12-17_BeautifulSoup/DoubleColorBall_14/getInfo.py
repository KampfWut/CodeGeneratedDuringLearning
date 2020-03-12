# Python 3.6.5

import urllib.request
from bs4 import BeautifulSoup
from saveExcel import SaveDoubleBallData
from myLog import myLog as mylog


class item(object):
    date = None
    idcore = None
    red1 = None
    red2 = None
    red3 = None
    red4 = None
    red5 = None
    red6 = None
    blue = None
    money = None
    firstPrize = None
    secondPrize = None

class getTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 15
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)
        self.log.info("> Save to excel ...")
        SaveDoubleBallData(self.items)

    # get all Url will be use 
    def getUrls(self, pageSum):
        urls = []
        pns = range(1, pageSum)
        ul = self.url.split("_")
        for pn in pns:
            ul[-1] = str(pn) + ".html"
            url = "_".join(ul)
            urls.append(url)
        self.log.info("> Get the Urls success.")
        return urls

    # spider web
    def spider(self, urls):
        self.log.info("> Start Spider.")
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tagsli = soup.find_all('tr', attrs = {})
            for tag in tagsli:
                if tag.find('em'):
                    i = item()

                    tagTd = tag.find_all('td')
                    i.date = tagTd[0].get_text()
                    i.idcore = tagTd[1].get_text()

                    tagEm = tagTd[2].find_all('em')
                    i.red1 = tagEm[0].get_text()
                    i.red2 = tagEm[1].get_text()
                    i.red3 = tagEm[2].get_text()
                    i.red4 = tagEm[3].get_text()
                    i.red5 = tagEm[4].get_text()
                    i.red6 = tagEm[5].get_text()
                    i.blue = tagEm[6].get_text()

                    i.money = tagTd[3].find('strong').get_text()
                    i.firstPrize = tagTd[4].find('strong').get_text()
                    i.secondPrize = tagTd[5].find('strong').get_text()

                    items.append(i)
                    self.log.info("> Get the item with date \"{}\" Success.".format(i.date))
        return items
    
    # save as file
    def pipelines(self, items):
        self.log.info("> Start Pipelines.")
        fileName = "14_DoubleColorBall.txt"
        f = open(fileName, 'w')
        for i in items:
            f.write("-" * 80)
            f.write("\ndate: {}\t id: {}\n".format(i.date, i.idcore))
            f.write("red: {} {} {} {} {} {} \t blue: {}\n".format(i.red1, i.red2, i.red3, i.red4, i.red5, i.red6, i.blue))
            f.write("Money: {}\t First Prize: {}\t Second Prize: {}\n".format(i.money, i.firstPrize, i.secondPrize))
            self.log.info("> Save date-\"{}\" in to file Success.".format(i.date))
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
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
    GTI = getTiebaInfo(url)
        


