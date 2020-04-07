def fizzbuzz(num):
    n = 1
    for n in range(n, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print 'fizz buzz'
        elif n % 3 == 0:
            print 'fizz'
        elif n % 5 == 0:
            print 'buzz'
        else: print n

import sys

for arg in sys.argv[1:]:
    print len(sys.argv[0:])
    if len(sys.argv) >= 2:
        fizzbuzz(int(sys.argv[1]))
    elif len(sys.argv) < 2:
        my_input = input('Please enter a number:')
        fizzbuzz(my_input)
