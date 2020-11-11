# Given an integer, n , print the decimal, octal, hex (capitalized),
# binary values for each integer i from 1 to n.
# The four values must be printed on a single line in the
# order specified above for each i from 1 to n. Each value should be
# space-padded to match the width of the binary value of n.

# Learn More: https://pyformat.info/
def print_formatted(number):
    s = len('{:b}'.format(number))
    print(s)
    for i in range(1, number+1):
        print('{:>{s}d} {:>{s}o} {:>{s}X} {:>{s}b}'.format(i, i, i, i, s=s))


n = int(input())
print_formatted(n)
