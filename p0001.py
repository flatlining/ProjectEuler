#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    total_sum = 0
    for n in range(0, 1000):
        if n%5 == 0 or n%3 == 0:
            total_sum += n
    print "> The sum of the multiples of 3 or 5 below 1000 is %s" % (total_sum)

# Simply starting at 3, saves 3 iterations
def RefinedOne():
    total_sum = 0
    for n in range(3, 1000):
        if n%5 == 0 or n%3 == 0:
            total_sum += n
    print "> The sum of the multiples of 3 or 5 below 1000 is %s" % (total_sum)

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
