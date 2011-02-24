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
    
    result = 0
    for i in range(2,2000001):
        if isPrime(i):
            result += i
    print "> The sum of all the primes below 2000000 is %s" % (result)

# Ignore even numbers
def RefinedOne():
    def isPrime(n):
        import math
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    result = 2
    for i in range(3,2000001,+1):
        if isPrime(i):
            result += i
    print "> The sum of all the primes below 2000000 is %s" % (result)

# Sieve of Eratosthenes > http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def RefinedTwo():
    def eratosthenes(nstart=2): # http://code.activestate.com/recipes/117119/
        D = {}
        q = nstart
        while 1:
            if q not in D:
                yield q
                D[q*q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p+q,[]).append(p)
                del D[q]
            q += 1
    
    eras = eratosthenes()
    result = 0
    for p in eras:
        if p >= 2000000:
            break
        result += p
    print "> The sum of all the primes below 2000000 is %s" % (result)

if __name__ == '__main__':
    import sys, re
    from timeit import Timer
    SOLUTION = "RefinedTwo"
    TESTS = 1
    PNUM = re.split("p0*", sys.argv[0].split(".")[0])[1]
    print ">>> Project Euler / Problem %s - http://projecteuler.net/index.php?section=problems&id=%s" % (PNUM, PNUM)
    t = Timer(SOLUTION + "()", "from __main__ import " + SOLUTION)
    elapsed = t.timeit(number=TESTS)/TESTS
    print ">>> Function %s() takes %0.5f seconds/pass" % (SOLUTION, elapsed)
