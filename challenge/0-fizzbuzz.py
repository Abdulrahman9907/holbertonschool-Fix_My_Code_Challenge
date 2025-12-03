#!/usr/bin/python3
import sys

def fizzbuzz(n):
    print(" ".join("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)))

if __name__ == '__main__':
    fizzbuzz(int(sys.argv[1]))
