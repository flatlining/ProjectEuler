#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    cstart = 1000
    for c in range(cstart, 0, -1):
        for b in range(c-1, 0, -1):
            for a in range(b-1, 0, -1):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print "> a(%s) * b(%s) * c(%s) = %s" % (a, b, c, a*b*c)
                    return

# Since a²+b²=c² (Pytagorean Triangle) we know that a+b > c, since a+b+c=1000 and a<b<c, we know that c<500
# According to Wikipedia (http://en.wikipedia.org/wiki/Pythagorean_triple#Elementary_properties_of_primitive_Pythagorean_triples) c is always odd, so we can decrease c in steps of 2 (since it begin in 499)
def RefinedOne():
    cstart = 499
    for c in range(cstart, 0, -2):
        for b in range(c-1, 0, -1):
            for a in range(b-1, 0, -1):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print "> a(%s) * b(%s) * c(%s) = %s" % (a, b, c, a*b*c)
                    return

# Wikipedia says: Exactly one of a, b is odd, so if b is even a will be odd, and if b is odd a will be even, since the first a in a iteration is always b-1 we can decrease a in steps of 2, eg: in a iteration that b is odd the first a will even and will always be, since even-2=even
def RefinedTwo():
    cstart = 499
    for c in range(cstart, 0, -2):
        for b in range(c-1, 0, -1):
            for a in range(b-1, 0, -2):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print "> a(%s) * b(%s) * c(%s) = %s" % (a, b, c, a*b*c)
                    return

if __name__ == '__main__':
    import sys, re
    from timeit import Timer
    SOLUTION = "RefinedTwo"
    TESTS = 1
    PNUM = re.split("p0*", sys.argv[0].split(".")[0])[1]
    print ">>> Project Euler / Problem %s - http://projecteuler.net/index.php?section=problems&id=%s" % (PNUM, PNUM)
    t = Timer(SOLUTION + "()", "from __main__ import " + SOLUTION)
    elapsed = t.timeit(number=TESTS)/TESTS
    print ">>> Function %s() takes %0.5f seconds/pass" % (SOLUTION, elapsed)
