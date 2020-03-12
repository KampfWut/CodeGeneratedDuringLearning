# Python 3.6.5

import urllib.request
from bs4 import BeautifulSoup
from myLog import myLog as mylog


class item(object):
    name = None
    score = None
    stars = None

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
        for pn in pns:
            url = self.url + str(pn) + ".html"
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
            tagsli = soup.find('ul', attrs = {"class":"v_picTxt pic180_240 clearfix"}).find_all('li')
            for tag in tagsli:
                if tag.find('div', attrs = {"class":"pic"}):
                    i = item()

                    i.name = tag.find('div', attrs = {"class":"txtPadding"}).find('em', attrs = {"class":"emTit"}).get_text()
                    i.score = tag.find('div', attrs = {"class":"pic"}).find('em').get_text()
                    tagSp = tag.find('div', attrs = {"class":"txtPadding"}).find("span", attrs = {"class":"sDes"}).find_all('em')
                    i.stars = ""
                    for t in tagSp:
                        i.stars = i.stars + t.a.get_text().strip() + ", "

                    items.append(i)
                    self.log.info("> Get the item with title \"{}\" Success.".format(i.name))
        return items
    
    # save as file
    def pipelines(self, items):
        self.log.info("> Start Pipelines.")
        fileName = "16_Movie.txt"
        f = open(fileName, 'w')
        for i in items:
            f.write("-" * 80)
            f.write("\ntitle: {}\t score: {}\n".format(i.name, i.score))
            f.write("stars: {}\n".format(i.stars[:-2]))
            self.log.info("> Save \"{}\" in to file Success.".format(i.name))
        f.close()

    # back url
    def getResponseContent(self, url):
        try:
            # Header
            head = {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
            Res = urllib.request.Request(url, headers = head)
            '''
            # Proxy
            proxy = urllib.request.ProxyHandler({"http":"http://113.65.5.47:9000"})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)
            '''
            
            res = urllib.request.urlopen(Res)
        except:
            self.log.error("> Back url Fail!")
        else:
            self.log.info("> Back url Success, Url is \"{}\".".format(url))
            # 注意编解码方式
            # 在各种浏览器打开的任意页面上使用F12功能键，即可使用开发者工具，在窗口console标签下，
            # 键入 "document.charset" 即可查看网页的编码方式。
            message = res.read().decode('GBK')
            '''
            # 删除注释， 防止soup读不到
            delstr = ["-->", "<!--"]
            for string in delstr:
                message = message.replace(string,"")
            '''
            return message

if __name__ == "__main__":
    # url不要使用utf-8格式的， 会失败
    url = "http://dianying.2345.com/list/----2018---"
    GTI = getTiebaInfo(url)
        


