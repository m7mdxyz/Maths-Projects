def add_binary_numbers(a, b):
    n = max(len(a), len(b))  # Find the maximum length of the binary numbers
    a = a.zfill(n)  # Zero-fill a to make it of length n
    b = b.zfill(n)  # Zero-fill b to make it of length n
    c = 0  # Initialize the carry
    result = []  # Initialize the result list

    for j in range(n - 1, -1, -1):
        aj = int(a[j])  # Convert the binary digit to an integer
        bj = int(b[j])  # Convert the binary digit to an integer
        d = (aj + bj + c) // 2
        sj = aj + bj + c - 2 * d
        c = d
        result.insert(0, sj)  # Insert at the beginning of the result list

    result.insert(0, c)  # Insert any remaining carry at the beginning

    return ''.join(map(str, result))  # Convert the result list to a binary string

# Example usage:
a = "1101"  # Binary number 1101
b = "1010"  # Binary number 1010
result = add_binary_numbers(a, b)
print(result)  # This will print the binary sum of a and b