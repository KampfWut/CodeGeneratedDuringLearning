import random, sys

class ChooseBall(object):
    def __init__(self):
        print("    >>> Choose ball <<<")
        self.processing()
    
    def processing(self):
        Flag = True
        
        while Flag:
            print("\n> Input the text times:")
            num_str = input("<<< ")

            num = 0
            while num == 0:
                try:
                    num = int(num_str)
                except ValueError:
                    print("> ERROR! You must input a number!")
                    sys.exit(1)

            ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(num):
                n = random.randint(1, 10)
                ball[n - 1] += 1

            print("> Finish!")    
            for i in range(1, 11):
                print(">   The probability of catching No. {:2d} ball is {:5f}.".format(i, ball[i - 1] / num))

            print("> Need again? (Y/N)")
            flag_str = input("<<< ")
            if flag_str[0].upper() == 'N':
                Flag = False


if __name__ == "__main__":
    c = ChooseBall()
