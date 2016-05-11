p = int(raw_input("Type P: "))
q = int(raw_input("Type Q: "))
e = int(raw_input("Type E: "))

def n(p,q):
    n = int(p)*int(q)
    return n

def phi(p,q):
    phi = (p-1)*(q-1)
    print phi
    return phi

def getE(phi):
    e = raw_input("Choose e: ")
    return e

def d(e, phi):
    d = 1
    while((e*d)%phi != 1):
        d += 1
    else:
        return d

print "Your private keys are: N=" + str(n(p, q)) + " and D=" + str(d(e, phi(p,q))) 
print "Your public keys are: E=" + str(e) + " and N=" + str(n(p,q))
