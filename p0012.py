#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    def factors(n): # Return the factors of a number, try to divide n from 2 to sqrt(n), if mod == 0 add as a divisor
        import math
        fact=[1,n]
        check=2
        rootn=math.sqrt(n)
        while check<rootn:
            if n%check==0:
                fact.append(check)
                fact.append(n/check)
            check+=1
        if rootn==check:
            fact.append(check)
        fact.sort()
        return fact
    
    def triNumbers(): # Return the triangle numbers
        top = 2
        while True:
            yield sum(range(1, top))
            top += 1
    
    tri = triNumbers()
    result = None
    divisors = None
    while True:
        n = tri.next()
        divisors = factors(n)
        if len(divisors) > 500:
            result = n
            break
    
    print "> The 1st triangle number to have over 500 divisors is (divisors: %s) %s" % (result, len(divisors) )

# Instead of calculating all the divisors, calculate the total number of divisors using prime factors > http://mathforum.org/library/drmath/view/56169.html
def RefinedOne():
    def numberOfDivisors(num):
        if num == 1: return 1
        import math
        def factorize(n):
            def isPrime(n):
                return not [x for x in xrange(2,int(math.sqrt(n))) if n%x == 0]
            primes = []
            candidates = xrange(2,n+1)
            candidate = 2
            while not primes and candidate in candidates:
                if n%candidate == 0 and isPrime(candidate):
                    primes = primes + [candidate] + factorize(n/candidate)
                candidate += 1            
            return primes
        pf = factorize(num)
        pf.sort()
        pows = []
        i = 0
        while i < len(pf):
            ocur = pf.count(pf[i])
            pows.append(ocur)
            i += ocur
        mult = 1
        for x in pows:
            mult *= x+1
        return mult
    
    def triNumbers(): # Return the triangle numbers
        top = 2
        while True:
            yield sum(range(1, top))
            top += 1
    
    tri = triNumbers()
    result = None
    divisors = None
    while True:
        n = tri.next()
        divisors = numberOfDivisors(n)
        if divisors > 500:
            result = n
            break
    
    print "> The 1st triangle number to have over 500 divisors is (divisors: %s) %s" % (result, divisors )

if __name__ == '__main__':
    import sys, re
    from timeit import Timer
    SOLUTION = "RefinedOne"
    TESTS = 1
    PNUM = re.split("p0*", sys.argv[0].split(".")[0])[1]
    print ">>> Project Euler / Problem %s - http://projecteuler.net/index.php?section=problems&id=%s" % (PNUM, PNUM)
    t = Timer(SOLUTION + "()", "from __main__ import " + SOLUTION)
    elapsed = t.timeit(number=TESTS)/TESTS
    print ">>> Function %s() takes %0.5f seconds/pass" % (SOLUTION, elapsed)
