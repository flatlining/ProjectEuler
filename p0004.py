#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    large = 0
    for n in range(999, 99, -1):
        for m in range(n, 99, -1):
            if str(m*n) == str(m*n)[::-1] and m*n > large:
                large = m*n
    print "> The largest palindrome from the product of two 3-digit numbers is %s" % (large)

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
