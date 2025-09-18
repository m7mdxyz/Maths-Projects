def gcd(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

# Example usage:
a = 48
b = 18
result = gcd(a, b)
print(f"GCD of {a} and {b} is {result}")