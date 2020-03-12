
class print9Plus9Table(object):
    def __init__(self):
        print("> Print the 9*9 table:")
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range (1, i + 1):
                print("{:2d} X {:2d} = {:2d}".format(j, i, i * j), end = "  ")
            print("\n", end = "")

if __name__ == "__main__":
    pro = print9Plus9Table()