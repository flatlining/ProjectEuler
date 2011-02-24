#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    def Divisors(n): return list(i for i in xrange(1, n/2+1) if n % i == 0)
    def D(n): return sum(Divisors(n))
    pairs = dict([ (n, D(n)) for n in range(1, 10001) ])
    soma = 0
    for n in pairs:
        if pairs[n] != n and pairs.get(pairs[n], 0) == n:
            soma += n
    print "> The sum from all amicable numbers from 1 to 10000 is %s" % (soma)

# A refined solution
def RefinedOne():
    import math
    def D(n): return sum(list(i for i in xrange(1, n/2+1) if n % i == 0))
    pairs = dict([ (n, D(n)) for n in range(1, 10001) ])
    soma = 0
    for n in pairs:
        if pairs[n] != n and pairs.get(pairs[n], 0) == n:
            soma += n
    print "> The sum from all amicable numbers from 1 to 10000 is %s" % (soma)

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
