#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one, brute force
def SimpleSolution():
    def isPrime(n):
        import math
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    primes = [2]
    n = 3
    while len(primes) < 10001:
        if isPrime(n):
            primes.append(n)
        n+=2
    
    print "> The 1001st prime is %s" % (primes[-1])

# A refined solution
def RefinedOne():
    print "> %s" % ()

if __name__ == '__main__':
    import sys, re
    from timeit import Timer
    SOLUTION = "SimpleSolution"
    TESTS = 1
    PNUM = re.split("p0*", sys.argv[0].split(".")[0])[1]
    print ">>> Project Euler / Problem %s - http://projecteuler.net/index.php?section=problems&id=%s" % (PNUM, PNUM)
    t = Timer(SOLUTION + "()", "from __main__ import " + SOLUTION)
    elapsed = t.timeit(number=TESTS)/TESTS
    print ">>> Function %s() takes %0.5f seconds/pass" % (SOLUTION, elapsed)
