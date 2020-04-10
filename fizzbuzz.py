# this here is written in Python 2 and needs changing

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

    # second try, closer to the mark
    
    import sys

inputs = sys.argv
inputs.pop(0)


def fizzbuzz(num):
    n = 0
    for n in range(n, num, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print ('fizzbuzz')
        elif n % 3 == 0:
            print ('fizz')
        elif n % 5 == 0:
            print ('buzz')
        else: print(n)

for arg in sys.argv:
        if len(sys.argv) >= 1:
            fizzbuzz(int(sys.argv[1]))
            
            
# someone made this one too - but it doesn't work; program runs too long and crashes

# The function accepts INTEGER n as parameter.
import sys

yx = sys.argv
yx.pop(0)


#

def fizzBuzz(yx):
    for i in yx:
        print(i)
        n = int(i) 
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz")
            elif x % 3 == 0:
                print("Fizz")
            elif x % 5 == 0:
                print("Buzz")
            else:
                print(x)


if __name__ == '__main__':
    yx = [input().strip()]

    fizzBuzz(yx)

    print(yx)
