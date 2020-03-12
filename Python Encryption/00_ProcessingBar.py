# Progress bar

import sys, time

'''
for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
'''

def numberBar(count, limited):
    sys.stdout.write("> Current progress： " + str(count) + "/" + str(limited) + '\r')
    sys.stdout.flush()

def symbolBar(count, limited):
    s1 = ""
    s2 = ""
    percent = round(count/limited,4)

    c = percent // 0.01
    s1 = '#' * int(c)
    s2 = '-' * (100 - int(c) - 1)

    sys.stdout.write("> " + s1 + s2 + "   " + str(round(percent * 100, 4)) + "% (" + str(count) + "/" + str(limited) + ")" + '\r')
    sys.stdout.flush()