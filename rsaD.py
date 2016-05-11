n=int(raw_input("Type N: "))
m=int(raw_input("Type M: "))

def inv(n,m,working):
	max=0
	val=0
	if (working==True):
		print "Val\t(val * n) mod m"
	while True:
		val = val + 1
		result = (val * n) % m
		if (working==True):
			print str(val)+"\t"+str(result)
		if (result==1):
        		break
		if (max>1500):
			return(0)
	return val

if (m<n):
	print "m need to be larger than n"
else:
	print "The inverse of "+str(n)+" mod "+str(m)+ " is " + str(inv(n,m,False))
	print "\nWorking out"
	print "Found it at "+str(inv(n,m,True))
