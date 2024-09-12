import math

def lcm (a,b):
    return abs(a*b) // math.gcd(a,b)


a = 25
b = 10
print(lcm(a,b))



def hcf(a,b):
    while b!=0:
        a,b =b, a%b
    return a

print(hcf(a,b))


