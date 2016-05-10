p = 29
q = 31
e = 283

def n(p,q):
    n = p*q
    return n

def phi(p,q):
    phi = (p-1)*(q-1)
    return phi

def getE(phi):
    e = raw_input("Choose e: ")
    return e

def d(e, phi):
    d=(e**(-1)) % phi
    return d

print "Your private keys are: N=" + str(n(p, q)) + " and D=" + str(d(e, phi(p,q))) 

