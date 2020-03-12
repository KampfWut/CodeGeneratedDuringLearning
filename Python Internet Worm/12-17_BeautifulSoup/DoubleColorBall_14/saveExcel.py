# Python 3.6.5

import xlwt

class SaveDoubleBallData(object):
    def __init__(self, items):
        self.items = items
        self.processing(self.items)

    def processing(self, items):
        fileName = "14_DoubleColorBall.xls"
        book = xlwt.Workbook(encoding = 'utf-8')
        sheet = book.add_sheet('DCBall', cell_overwrite_ok = True)

        sheet.write(0, 0, "开奖日期")
        sheet.write(0, 1, "期号")
        sheet.write(0, 2, "红色球1")
        sheet.write(0, 3, "红色球2")
        sheet.write(0, 4, "红色球3")
        sheet.write(0, 5, "红色球4")
        sheet.write(0, 6, "红色球5")
        sheet.write(0, 7, "红色球6")
        sheet.write(0, 8, "蓝色球")
        sheet.write(0, 9, "奖池")
        sheet.write(0, 10, "一等奖人数")
        sheet.write(0, 11, "二等奖人数")

        i = 1
        while i <= len(items):
            it = items[i - 1]
            sheet.write(i, 0, it.date)
            sheet.write(i, 1, it.idcore)
            sheet.write(i, 2, it.red1)
            sheet.write(i, 3, it.red2)
            sheet.write(i, 4, it.red3)
            sheet.write(i, 5, it.red4)
            sheet.write(i, 6, it.red5)
            sheet.write(i, 7, it.red6)
            sheet.write(i, 8, it.blue)
            sheet.write(i, 9, it.money)
            sheet.write(i, 10, it.firstPrize)
            sheet.write(i, 11, it.secondPrize)
            i = i + 1
        
        book.save(fileName)

if __name__ == "__main__":
    pass








