c = int(raw_input("Type C: "))
d = int(raw_input("Type D: "))
n = int(raw_input("Type N: "))

def dec(c,d,n):
    m = (int(c)**int(d)) % int(n)
    return m

print "M=" + str(dec(c,d,n))
