#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
# Ok, I cheated in this one, credit goes to http://dannyturner.net/?entry=entry090723-161119
    import math
    C = lambda n, r : (math.factorial(n)/(math.factorial(r)*math.factorial(n - r)))
    print "> There are %s routes" % (C(40,20))

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
