# -*- coding: utf-8 -*-
"""task3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tq9b40Af8cSd5JVYlVPpsMO-pJIMNQmH
"""

def fibonacci(limit):
    # Initialize the first two Fibonacci numbers
    fib_list = [0, 1]

    # Generate Fibonacci sequence
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > limit:
            break
        fib_list.append(next_fib)

    return fib_list

# Example usage:
limit = 100  # Change this to any limit you want
fib_sequence = fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fib_sequence)