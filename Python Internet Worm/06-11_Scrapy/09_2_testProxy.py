# Python 3.6.5
# Test Proxy

import urllib.request
import re
import threading

count = 0
limited = 0

class testProxy(object):
    def __init__(self):
        self.readFile = "./GetProxyProject_09/use_proxy.txt"
        self.saveFile = "./GetProxyProject_09/alive_proxy.txt"
        self.testUrl = "http://www.baidu.com"
        self.thread = 10
        self.timeout = 5
        self.regex = re.compile('baidu.com')
        self.alive = []
        self.threadList = []
        self.process()

    # main processing
    def process(self):
        f1 = open(self.readFile, 'r')
        lines = f1.readlines()
        global limited
        limited = len(lines)
        line = lines.pop()
        while lines:
            for i in range(self.thread):
                t = threading.Thread(target = self.linkWithProxy, args = (line,))
                self.threadList.append(t)
                t.start()
                if lines:
                    line = lines.pop()
                else:
                    continue
        f1.close()

        # main thread waitting finish
        for i in self.threadList:
            i.join()          

        print("-" * 50)
        print("> Save Alive ...")

        f2 = open(self.saveFile, 'w')
        for i in self.alive:
            f2.write(i)
        f2.close()
        print("-" * 50)

    # subthread
    def linkWithProxy(self, line):
        global count 
        global limited

        lineList = line[1:-3].split(':')
        ip = lineList[0]
        port = lineList[1]
        protocol = lineList[2].lower()
        server = protocol + "://" + ip + ":" + port
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol:server}))
        urllib.request.install_opener(opener)

        try:
            res = urllib.request.urlopen(self.testUrl, timeout = self.timeout)
        except:
            count = count + 1
            print("> [{:4d}/{:4d}] \"{}\" connection failed.".format(count, limited, server))
            return
        else:
            try:
                string = res.read().decode('utf-8')
            except:
                count = count + 1
                print("> [{:4d}/{:4d}] \"{}\" connection failed.".format(count, limited, server))
                return
            if self.regex.search(string):
                count = count + 1
                print("> [{:4d}/{:4d}] \"{}\" connection success!".format(count, limited, server))
                self.alive.append(line)

if __name__ == "__main__":
    tp = testProxy()


