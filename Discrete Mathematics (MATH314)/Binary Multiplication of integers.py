def add_binary_numbers(a, b):
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    carry = 0
    result = []

    for j in range(n - 1, -1, -1):
        bit_sum = int(a[j]) + int(b[j]) + carry
        result.insert(0, str(bit_sum % 2))
        carry = bit_sum // 2

    if carry:
        result.insert(0, '1')

    return ''.join(result)

def multiply_binary_numbers(a, b):
    n = len(a)
    m = len(b)

    # Initialize the product as a string of zeros
    product = '0' * (n + m)

    for j in range(m - 1, -1, -1):
        if b[j] == '1':
            # Shift 'a' left by 'm - 1 - j' positions
            shifted_a = a + '0' * (m - 1 - j)
            # Add the shifted 'a' to the product
            product = add_binary_numbers(product, shifted_a)

    return product

# Example usage:
a = "1101"  # Binary number 1101
b = "1010"  # Binary number 1010
result = multiply_binary_numbers(a, b)
print(result)  # This will print the binary product of a and b