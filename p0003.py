#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one, http://en.wikipedia.org/wiki/Prime_factor
def SimpleSolution():
    # From here http://www.indopedia.org/Prime_factorization_algorithm.html
    def factorize(n):
        def isPrime(n): return ( False if n < 2 else not [x for x in xrange(2,int(n**0.5)+1) if n%x == 0] )
        primes = []
        candidates = xrange(2,n+1)
        candidate = 2
        while not primes and candidate in candidates:
            if n%candidate == 0 and isPrime(candidate):
                primes = primes + [candidate] + factorize(n/candidate)
            candidate += 1            
        return primes
    
    n = 600851475143
    result = max(factorize(n))
    print "> largest prime factor of %s is %s" % (n, result)

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
