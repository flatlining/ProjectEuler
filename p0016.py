#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    soma = 0
    for d in str(2**1000):
        soma += int(d)
    print "> The sum of the digits of 2^1000 is %s" % (soma)

# One line python
def RefinedOne():
    print "> The sum of the digits of 2^1000 is %s" % (sum(int(digit) for digit in str(2**1000)))

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
