# Base Prime Number Sieve

import math

# Judge is a prime num or not 
def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):

    sieve = [True] * sieveSize
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer = pointer + i

    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes

if __name__ == "__main__":
    print("> Judge num: ")
    num_str = input("<<< ")
    num = int(num_str)
    print("> {}".format(isPrime(num)))

    print("> {}".format(primeSieve(num)))