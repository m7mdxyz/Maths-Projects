def base_b_expansion(n, b):
    q = n
    result = 0
    multiplier = 1

    while q != 0:
        ak = q % b
        q = q // b  # Using integer division
        result += ak * multiplier
        multiplier *= 10  # Update the multiplier for the next digit

    return result

# Example Usage:
n = 1017  # The number to be converted
b = 2  # The base
result = base_b_expansion(n, b)
print(result)  # This will print the base-b expansion of n as an integer