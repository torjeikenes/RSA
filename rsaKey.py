from fractions import gcd
from random import randint

def getE():
    e = int(raw_input("Input E: "))
    if(gcd(e, phi(p,q)) == 1):
        return e
    else:
        print "E must not share any common factors with N. Try again"
        getE()

def randomE():
    e = randint(2, phi(p,q))
    print e
    if(gcd(e, phi(p,q)) == 1):
        return e
    else:
        randomE()

def getNum(letter):
    num = raw_input("Input " + letter + ": ")
    if(isPrime(num) == False):
        print num + " is not a prime number. Try Again"
        getNum(letter)
    else:
        return int(num)

def randomNum():
    num = randint(1000, 9999)
    while(isPrime(num) == False):
        num += 1
    else:
        return int(num)


def isPrime(num):
    prime = True
    for i in range(2, int(num)):
        if(int(num) % i == 0):
            prime = False
    return prime


def phi(p,q):
    phi = (p-1)*(q-1)
    return phi

rand = raw_input("Do you want to choose your own P, Q and E? (y,n)")
if(rand == "y"):
    p = getNum("P")
    q = getNum("Q")
    e = getE()
else:
    p = randomNum()
    print "p " + str(p)
    q = randomNum()
    print "q " + str(q)
    e = randomE()

def n(p,q):
    n = int(p)*int(q)
    return n

def d(e, phi):
    d = 1
    while((e*d)%phi != 1):
        d += 1
    else:
        return d

n = n(p,q)
d = d(e, phi(p,q))


print "Your private keys are: N=" + str(n) + " and D=" + str(d)
print "Your public keys are: E=" + str(e) + " and N=" + str(n)

c = int(raw_input("Type C: "))

def dec(c,d,n):
    m = (int(c)**int(d)) % int(n)
    print m
    return m

print "M=" + str(dec(c,d,n))
