# -*- coding: utf-8 -*-
"""task 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tq9b40Af8cSd5JVYlVPpsMO-pJIMNQmH
"""

def print_positive_numbers(start, end):
    if start > end:
        print("Invalid range: Start should be less than or equal to end.")
        return

    print("Positive numbers in the range from", start, "to", end, "are:")
    for num in range(start, end + 1):
        if num > 0:
            print(num)

# Example usage:
start = -5
end = 10
print_positive_numbers(start, end)