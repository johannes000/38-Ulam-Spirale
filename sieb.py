import time
import math
#TODO: Multithreading
def gen_prime_list(n):
	nsqrt = int(math.sqrt(n))
	nummern = []
	for x in range(1,n):
		nummern.append(x)

	for x in range(2,nsqrt):
		for y in nummern:
			if y%x == 0 and not y==x:
				nummern.remove(y)
	return nummern		
