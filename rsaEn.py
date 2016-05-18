e = int(raw_input("Type E: ")) 
n = int(raw_input("Type N: ")) 

def getM(n):
    m = int(raw_input("Type M: "))    
    if(m < n):
        return m
    else:
        print "m must be smaller than n."
        exit()

m = getM(n)


def enc(e,n,m):
    c = (int(m)**int(e)) % int(n)
    return c

print " C=" + str(enc(e,n,m))
