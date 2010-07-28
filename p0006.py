#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one
def SimpleSolution():
    sum_of_squares = 0
    # Sum of the squares
    for n in range(1,101):
        sum_of_squares += n**2
    # Square of sums ()n(n+1))/2
    square_of_sum = (50 * 101)**2
    result = sum_of_squares - square_of_sum
    print "> %s - %s = %s" % (sum_of_squares, square_of_sum, result)

# Use mathematical optimization
def RefinedOne():
    n=100
    # Sum of the squares, sum of the square of all integers from 1 to n = (n*(n+1)*(2*n+1))/6
    sum_of_squares = (n*(n+1)*(2*n+1))/6
    # Square of sums, sum of all integers from 1 to n = (n*(n+1))/2
    square_of_sum = ((n*(n+1))/2)**2
    result = sum_of_squares - square_of_sum
    print "> %s - %s = %s" % (sum_of_squares, square_of_sum, result)

def RefinedThree():
    sum_of_squares = sum([x**2 for x in range(1,101)]) 
    square_of_sum = sum(range(1,101))**2
    result = sum_of_squares - square_of_sum
    print "> %s - %s = %s" % (sum_of_squares, square_of_sum, result)

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
