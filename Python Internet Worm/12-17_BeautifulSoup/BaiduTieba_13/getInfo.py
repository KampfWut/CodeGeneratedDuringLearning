# Python 3.6.5

import urllib.request
from bs4 import BeautifulSoup
from myLog import myLog as mylog


class item(object):
    title = None
    author = None
    time = None
    reNum = None
    lastReContent = None
    lastAuthor = None
    lastReTime = None

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
        pns = [str(i * 50) for i in range(pageSum)]
        ul = self.url.split("=")
        for pn in pns:
            ul[-1] = pn
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
            tagsli = soup.find_all('li', attrs = {"class":" j_thread_list clearfix"})
            for tag in tagsli:
                i = item()
                i.title = tag.find('a', attrs = {"class":"j_th_tit"}).get_text().strip()
                i.author = tag.find('span', attrs = {"class":"frs-author-name-wrap"}).a.get_text().strip()
                i.time = tag.find('span', attrs = {"title":"创建时间"}).get_text().strip()
                i.reNum = tag.find('span', attrs = {"title":"回复"}).get_text().strip()
                i.lastReContent = tag.find('div', attrs = {"class":"threadlist_abs threadlist_abs_onlyline "}).get_text().strip()
                i.lastAuthor = tag.find('span', attrs = {"class":"tb_icon_author_rely j_replyer"}).a.get_text().strip()
                i.lastReTime = tag.find('span', attrs = {"title":"最后回复时间"}).get_text().strip()
                items.append(i)
                self.log.info("> Get the item with title \"{}\" Success.".format(i.title))
        return items
    
    # save as file
    def pipelines(self, items):
        self.log.info("> Start Pipelines.")
        fileName = "13_DLUTbaidutb.txt"
        f = open(fileName, 'w')
        for i in items:
            f.write("-" * 80)
            f.write("\ntitle: {}\t author: {}\t firstTime: {}\t return number: {}\n".format(i.title, i.author, i.time, i.reNum))
            f.write("content:\n{}\n".format(i.lastReContent))
            f.write("lastAuthor: {}\t lastTime: {}\n\n".format(i.lastAuthor, i.lastReTime))
            self.log.info("> Save \"{}\" in to file Success.".format(i.title))
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
            # 删除注释， 防止soup读不到
            delstr = ["-->", "<!--"]
            for string in delstr:
                message = message.replace(string,"")

            return message

if __name__ == "__main__":
    # url不要使用utf-8格式的， 会失败
    url = "http://tieba.baidu.com/f?kw=%E5%A4%A7%E8%BF%9E%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=0"
    GTI = getTiebaInfo(url)
        


