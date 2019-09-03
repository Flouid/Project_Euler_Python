import time

'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Louis Keith
8-3-19
'''


class Problem76:

    # the presentation of the example implies that there is a pattern to the way the number of sums expand with n
    # it seems the rough algorithm is as follows: the first sum is always (n - 1 + 1), the second is n - 2, (1 + 1)),
    # where all ways of writing 1 + 1 are valid (ie. '1 + 1' and '2')
    # it appears this pattern continues with the first term decrementing while the second term is any and all ways
    # of writing the difference between the first time and n.
    # that doesn't really make sense so...

    # the sequence always goes like this for some n: (n - 1) + 1, (n - 2) + all the ways of writing the sum of 2
    # what im saying is that there will be a 'n - 2' term for every way you could write the sum of 2
    # similarly, there will be a 'n - 3' term for every way you could write the sum of 3
    # i will shorthand every way you could write a number n as all_ways_n

    # what this all means is the values of all_ways_n from 2 to 100 are necessary for the calculation and can be
    # easily successively generated

    #################################################################################################################

    # ok I worked through that and while there's probably an inelegant way to get it to work it involves dealing with
    # the problem of double counting solutions. Instead I explored other options and discovered dynamic programming.

    # the basic concept is that you work off of a list that stores the number of solutions for any given n.
    # this list is generated by going through and adding all the ways to write each integer with each other integer.
    # it saves a ton of calculations though by always being able to reference values it has already had to calculate
    # and change them when new solutions are found

    # beautiful solution, i wish i had come up with it on my own. below is a link to the resource i used
    # https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/

    @staticmethod
    def main():
        start = time.time()

        target = 100
        ways = [0 for i in range(target + 1)]
        # this behaves like a simplified recursive algorithm, this is analogous to the base case
        ways[0] = 1
        for i in range(1, target):
            j = i
            while j <= target:
                ways[j] += ways[j - i]
                j += 1
        # the last element in the list will be the number of ways to write the last element calculated, the target
        print(ways[len(ways) - 1])

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem76.main()
