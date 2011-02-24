#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    def Check(n):
        for d in range(20,1,-1):
            if n%d != 0:
                return False
        return True
    
    n = 19
    while not Check(n):
        n += 1
    print "> The smallest number that is divided by 1 to 20 is %s" % (n)

# Uses GCD, LCM and python reduce function (http://docs.python.org/library/functions.html)
def RefinedOne():
    # Return Greatest Common Divisor (http://en.wikipedia.org/wiki/Binary_GCD_algorithm)
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a 
    # Return Least Common Multiple (http://en.wikipedia.org/wiki/Least_common_multiple)
    def lcm(a, b):
        return a*b/gcd(a, b) 
    
    result = reduce(lcm, range(1, 20+1))
    print "> The smallest number that is divided by 1 to 20 is %s" % (result)

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
