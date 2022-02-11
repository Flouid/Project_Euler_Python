"""
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first
one hundred decimal digits for all the irrational square roots.

Louis Keith
2-11-22
"""

from time import time
import math


def main():
    print(math.e**(0.5 * math.log(2)))



if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))
