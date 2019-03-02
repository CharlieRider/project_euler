"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""
from functools import reduce

def largest_divisors(n):
    possible_large_divisors = list(range(1, n+1))
    for i in range(n, 0, -1):
        if i in possible_large_divisors:
            for j in range(1, i):
                if i %j == 0:
                    if j in possible_large_divisors:
                        possible_large_divisors.remove(j)
    return possible_large_divisors


def smallest_possible_multiple(n):
    must_fit_divisors = largest_divisors(n)
    largest_divisor = must_fit_divisors[-1]
    largest_possible = reduce(lambda x,y: x*y, must_fit_divisors)
    possible_iterations = int(largest_possible / largest_divisor)
    print(possible_iterations)
    for i in range(1, possible_iterations):
        possible_match = largest_divisor * i
        if all([possible_match % x ==0 for x in must_fit_divisors]):
            return possible_match


print(smallest_possible_multiple(20))