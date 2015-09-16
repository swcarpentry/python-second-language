# Profiling pi methods
# mw 20150916

import math
import random
import decimal

@profile
def montecarlo(maxIt):
	ctr = 0
	variance = 3.141
	for i in range(maxIt):
    		if math.pow(random.random(), 2.0) + math.pow(random.random(), 2.0) <= 1.0:
        		ctr += 1
			result = (4.0 * ctr / maxIt)
			if abs(math.pi - result) <= variance:
				variance = abs(math.pi - result)
				cbest=result
	print " Monte Carlo method: "+str(cbest)

@profile
def archie(prec):
	decimal.getcontext().prec = prec
	D=decimal.Decimal

	eps = D(1)/D(10**prec)

	x = D(4)
	y = D(2)*D(2).sqrt()

	ctr = D(0)
	while x-y > eps:
		xnew = 2*x*y/(x+y)
		y = D(xnew*y).sqrt()
		x = xnew
		ctr +=1
	print "  Archimedes method: "+ str((x+y)/D(2))

montecarlo(1000000) # number of iterations for the monte carlo routine to run
archie(8) # level of precision, eg 8 decimal places
print " Python value of pi: "+str(math.pi)[:9] # the value of pi in math.pi
