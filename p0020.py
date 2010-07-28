#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    def factorial(n): return reduce(lambda x,y:x*y,range(1,n+1))
    
    result = 0
    for d in str(factorial(100)):
        result += int(d)
    print "> The sum of the digits of 100! is %s" % (result)

# Calculating recursively
def RefinedOne():
    def fact(x): return (1 if x==0 else x * fact(x-1))
    print "> The sum of the digits of 100! is %s" % ( reduce( lambda x, y : int(x)+int(y), str(fact(100)) ) )

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
