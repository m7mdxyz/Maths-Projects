def horner(poly, n, x):
    # Initialize result
    result = poly[0]
    
    for i in range(1, n):
        result = result * x + poly[i]
    return result

# Evaluating polynomial x^4 - 4x^3 + 7x^2 - 5x - 2 at r = 3
p = [1, -4, 7, -5, -2]
r = 3
n = len(p)
print("Value of polynomial is ", horner(p, n, r))