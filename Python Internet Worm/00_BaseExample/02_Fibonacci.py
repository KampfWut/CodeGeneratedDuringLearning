import sys

class Fibonacci(object):

    def __init__(self):
        print("   >>> Fibonacci list <<<")
        self.list = [0, 1]
        self.processing()

    def processing(self):
        print("> Please input the length of Fibonacci list:")
        length_str = input("<<< ")

        length = 0
        while length == 0:
            try:
                length = int(length_str)
            except ValueError:
                print("> ERROR! you should input a number!")
        
        self.checkInput(length)

        while len(self.list) < length:
            self.list.append(self.list[-1] + self.list[-2])
        print("> Finish!\n> Fibonacci list: {}".format(self.list))

    def checkInput(self, length):
        if length not in range(3,51):
            print("> Input best least than 50 and bigger than 3.")
            sys.exit(1)

if __name__ == "__main__":
    f = Fibonacci()
            
        