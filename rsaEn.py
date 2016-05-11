e = int(raw_input("Type E: ")) 
n = int(raw_input("Type N: ")) 
m = int(raw_input("Type M: "))

def enc(e,n,m):
    c = (int(m)**int(e)) % int(n)
    return c

print " C=" + str(enc(e,n,m))
