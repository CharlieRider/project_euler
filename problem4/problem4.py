"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_numeric_palindrome(n):
    str_n = str(n)
    if len(str(n)) % 2 == 0:
        first_split_reversed = "".join(reversed(str_n[:int(len(str_n) / 2)]))
        second_split = str_n[int(len(str_n) / 2):]
        if first_split_reversed == second_split:
            return True
    return False

def largest_multiplicative_palindrome(num_digits):
    max_range = int('9' * num_digits)
    largest_palindrome = 0
    for x in range(max_range, -1, -1):
        for y in range(max_range, -1, -1):
            multiple = x * y
            if is_numeric_palindrome(multiple):
                if multiple > largest_palindrome:
                    largest_palindrome = multiple
    return largest_palindrome

largest_multiplicative_palindrome(3)
