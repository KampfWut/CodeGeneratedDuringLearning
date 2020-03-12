# Python 3.6.5

import re
import sys
from urllib import error, request

import use_py.userAgents

class changeHeader(object):
    def __init__(self):
        print("    >>> Change Header <<<")
        PIUA = use_py.userAgents.pcUserAgent.get("IE 9.0")
        MUUA = use_py.userAgents.mobileUserAgent.get("UC standard")
        self.url = "http://fanyi.youdao.com"

        print("> A. PIUA, header :")
        print(PIUA)
        self.useUserAgent(PIUA, "PIUA")
        print("> B. MUUA, header :")
        print(MUUA)
        self.useUserAgent(MUUA, "MUUA")

    def useUserAgent(self, userAgent, name):
        print("> Connecting......", end = "")
        res = request.Request(self.url)
        res.add_header(userAgent.split(":")[0], userAgent.split(":")[1])
        
        fd = request.urlopen(res)
        print("\t[Success]")
         
        fileName = "03_" + str(name) + ".html"
        f = open(fileName, "w")
        f.write("{}\n\n".format(userAgent))
        f.write(fd.read().decode("utf-8"))
        f.close()

if __name__ == "__main__":
    u = changeHeader()

