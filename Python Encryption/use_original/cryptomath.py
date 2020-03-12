# GCD & Inverse mod

def gcd(a, b):
    while a != 0:
        a, b = b%a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q*v1), (u2 - q*v2), (u3 - q*v3), v1, v2, v3
    return u1 % m

if __name__ == "__main__":
    print("> GCD\n> input a and b:")
    a = input("a <<< ")
    a = int(a)
    b = input("b <<< ")
    b = int(b)
    ans = gcd(a,b)
    print("> GCD answer is {}".format(ans))

    print("> Inverse Mod\n> input a and m:")
    a = input("a <<< ")
    a = int(a)
    m = input("m <<< ")
    m = int(b)
    ans = findModInverse(a,m)
    print("> Inverse Mod answer is {}".format(ans))