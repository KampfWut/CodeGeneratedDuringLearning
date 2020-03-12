# Python 3.6.5

import os
import platform
import sys
import time
import urllib
from urllib import error, request, response


# Use to clean screen
def clear():
    print("> Warning! Too many information, we turn over after 3 second.")
    time.sleep(3)
    OS = platform.system()
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# main processing
def linkBaidu():
    print("> Link to Baidu...", end="")
    url = "http://www.baidu.com"

    try:
        req = request.Request(url)
    except error.URLError:
        print("> Connection failed!")
        sys.exit(1)
    print("\t[Success]")

    print("> Get the message......", end="")
    fd = request.urlopen(req)
    orignalMessage = fd.read()
    useMessage= orignalMessage.decode("utf-8")
    print("\t[Success]")
    
    f = open("./01_baidu.txt", "wb")
    f.write(orignalMessage)
    f.close()

    print("> Get the URL information : {}".format(fd.geturl()))
    print("> Get the back code       : {}".format(fd.getcode()))
    print("> Get the back information: \n{}".format(fd.info()))
    print("> Message has save in the 01_baidu.txt")
    

if __name__ == "__main__":
    linkBaidu()
