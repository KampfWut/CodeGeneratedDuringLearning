# Python 3.6.5

import time
import urllib.request
from bs4 import BeautifulSoup
from myLog import myLog as mylog


class item(object):
    top_num = None
    score = None
    mvName = None
    singer = None
    time = None


class getTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 4
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
            tagsli = soup.find('ul', attrs = {"class":"area_three area_list"}).find_all('li')
            for tag in tagsli:
                i = item()

                i.top_num = tag.find('div', attrs = {"class":"top_num"}).get_text()
                i.score = tag.find('div', attrs = {"class":"score_box"}).h3.get_text()
                i.mvName = tag.find('div', attrs = {"class":"info"}).h3.a.get_text()
                i.singer = ""
                tagP = tag.find('p', attrs = {"class":"cc"}).find_all('a', attrs = {"class":"special"})
                for ta in tagP:
                    i.singer = i.singer + ta.get_text() + ", "
                i.time = tag.find('p', attrs = {"class":"c9"}).get_text().replace("发布时间：", "")

                items.append(i)
                self.log.info("> Get the item with name \"{}\" Success.".format(i.mvName))
        return items
    
    # save as file
    def pipelines(self, items):
        self.log.info("> Start Pipelines.")
        fileName = "17_MVBang.txt"
        f = open(fileName, 'w')
        for i in items:
            f.write("-" * 80)
            f.write("\nmv name: {}\t top number: {}\t score : {}\n".format(i.mvName, i.top_num, i.score))
            f.write("singer: {}\t create time: {}\n".format(i.singer[:-2], i.time))
            self.log.info("> Save \"{}\" in to file Success.".format(i.mvName))
        f.close()

    # back url
    def getResponseContent(self, url):
        try:
            # Header
            head = {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
            Res = urllib.request.Request(url, headers = head)
            
            # Proxy
            # proxy = urllib.request.ProxyHandler({"http":"http://113.65.5.47:9000"})
            # opener = urllib.request.build_opener(proxy)
            # urllib.request.install_opener(opener)
            
            res = urllib.request.urlopen(Res)
            # 暂停1s
            time.sleep(1)
        except:
            self.log.error("> Back url Fail!")
        else:
            self.log.info("> Back url Success, Url is \"{}\".".format(url))
            # 注意编解码方式
            # 在各种浏览器打开的任意页面上使用F12功能键，即可使用开发者工具，在窗口console标签下，
            # 键入 "document.charset" 即可查看网页的编码方式。
            message = res.read().decode('utf-8')
            '''
            # 删除注释， 防止soup读不到
            delstr = ["-->", "<!--"]
            for string in delstr:
                message = message.replace(string,"")
            '''
            return message

if __name__ == "__main__":
    # url不要使用utf-8格式的， 会失败
    url = "http://vchart.yinyuetai.com/vchart/trends?area=ALL&page=1"
    GTI = getTiebaInfo(url)
        


