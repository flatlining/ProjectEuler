#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Matias Schertel (flatlining@ProjectEuler) - mschertel@gmail.com

# Most simple one, using iteration for calculatin hailstone sequences > http://en.wikipedia.org/wiki/Collatz_conjecture
def SimpleSolution():
    def sequence(seed, current = None): # Calculate the sequence starting at seed
        if not current: # If first time function is call create var tu save sequence
            current = []
        current.append(seed)
        if seed == 1: # if current number equal 1 return the complete sequence
            return current
        elif seed % 2: # if current number current is odd, 3n+1 and call the function again
            return sequence(3*seed+1, current)
        else: # if current number is even, 2n and call the function again
            return sequence(seed/2, current)
    
    upper = 1000000
    result = 0, []
    for sn in range(1, upper+1):
        seq = sequence(sn)
        if len(seq) > len(result[1]):
            result = sn, seq
    print "> The starting number, under 1KK, which produces the longest chain is %s (length: %s)" % ( result[0] , len(result[1]) ) # To print the sequence use: ", ".join([str(i) for i in result[1]])

# Equal from the upper one but starts at 500,001, because:
# Reasoning for choosing 500,001 and odd numbers were was based on -> every number n under 500,000 has corresponding reverse map 2n in upper half.-> Odd number n, reverse maps to and even number in upper half which in turn maps to a number in lower half.
def RefinedOne():
    def sequence(seed, current = None):
        if not current:
            current = []
        current.append(seed)
        if seed == 1:
            return current
        elif seed % 2:
            return sequence(3*seed+1, current)
        else:
            return sequence(seed/2, current)
    
    upper = 1000000
    result = 0, []
    for sn in range(upper/2+1, upper+1, 2):
        seq = sequence(sn)
        if len(seq) > len(result[1]):
            result = sn, seq
    print "> The starting number, under 1KK, which produces the longest chain is %s (length: %s)" % ( result[0] , len(result[1]) )

# Using a hash table > http://projecteuler.net/index.php?section=forum&id=14&page=2, strarting at 500001
collatz = {1:1}
def RefinedTwo():
    def Collatz(n):
        global collatz
        if not collatz.has_key(n):
            if n%2 == 0:
                collatz[n] = Collatz(n/2) + 1
            else:
                collatz[n] = Collatz(3*n + 1) + 1
        return collatz[n]
    
    upper = 1000000
    for j in range(upper/2+1, upper+1, 2):
        Collatz(j)
    result = collatz.keys()[collatz.values().index(max(collatz.values()))], max(collatz.values())
    print "> The starting number, under 1KK, which produces the longest chain is %s (length: %s)" % ( result[0], result[1] )

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
