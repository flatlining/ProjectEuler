#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    import datetime
    sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                sundays = sundays + 1
    print "> The number of Sundays that are the 1st day of a month between 1900 and 2001 is %s" % (sundays)

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
