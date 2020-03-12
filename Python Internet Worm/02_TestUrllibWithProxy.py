# Python 3.6.5

import re
import sys
from urllib import error, request

class testProxy(object):
    def __init__(self, proxy):
        self.proxy = proxy
        self.checkProxyFormat(self.proxy)
        self.url = "http://www.baidu.com"
        self.timeout = 10
        self.keyWord = "百度"
        self.useProxy(self.proxy)

    def checkProxyFormat(self, proxy):
        try:
            proxyMatch = re.compile("http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$")
            re.search(proxyMatch, proxy).group()
        except AttributeError:
            print("> Can\'t match the input proxy")
            sys.exit(1)

        flag = True
        proxy = proxy.replace("//","")
        try:
            protocol = proxy.split(":")[0]
            ip = proxy.split(":")[1]
            port = proxy.split(":")[2]
        except IndexError:
            print("> ERROR! Overflow!")
            sys.exit(2)
        
        print("> Start check......")
        # check format
        flag = flag and len(proxy.split(":")) == 3 and len(ip.split("."))
        flag = flag and int(ip.split(".")[0]) in range(1, 256)
        flag = flag and int(ip.split(".")[1]) in range(256)
        flag = flag and int(ip.split(".")[2]) in range(256)
        flag = flag and int(ip.split(".")[3]) in range(1, 256)
        flag = flag and protocol in ["http", "https"]
        flag = flag and int(port) in range(1, 65535)

        if flag:
            print("> Check finish! This proxy can be used!")
            print(">   Protocol : \t\t{}\n>   IP : \t\t{}\n>   Port : \t\t{}".format(protocol, ip, port))
        else:
            print("> Check failed! illegal proxy!")

    def useProxy(self, proxy):
        protocol = proxy.split(":")[0].replace(":", "")
        ip = proxy.split(":")[1]

        print("> Connecting......", end = "")
        fd = request.build_opener(request.ProxyHandler({protocol:ip}))
        request.install_opener(fd)
        try:
            res = request.urlopen(self.url, timeout = self.timeout)
        except:
            print("\t[Failed]")
            print("> ERROR! Url open failed! ")
            sys.exit(3)
        print("\t[Success]")

        originalMessage = res.read()
        useMessage = originalMessage.decode("utf-8")
        if re.search(self.keyWord, useMessage):
            print("> Get the Key word! This proxy can conection.")
        else:
            print("> Fail to get key word! This proxy can\'t conection.")


if __name__ == "__main__":
    print("    >>> Test proxy <<<")
    print("> input the proxy address as \"http[s]://1.2.3.4:5 :\"")
    proxy = input("<<< ")
    t = testProxy(proxy)
        


