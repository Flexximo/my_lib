def is_even(n):
    return n == 0 if n <= 1 else is_odd(n - 1)
def is_odd(n):
    return n == 1 if n <= 1 else is_even(n - 1)

assert is_even == False, "The number is not even"
is_even(98)