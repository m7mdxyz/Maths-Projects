def modular_exponentiation(b, n, m):
    x = 1
    power = b % m

    for ai in reversed(n):  # Reversed to start with the least significant bit
        if ai == '1':
            x = (x * power) % m
        power = (power * power) % m

    return x

# Example usage:
b = 3  # Base
n = "1101"  # Exponent in binary
m = 7  # Modulus
result = modular_exponentiation(b, n, m)
print(result)  # This will print the result of (b^n) % m