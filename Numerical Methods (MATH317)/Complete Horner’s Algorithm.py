def horner(poly, n, r):
    result = poly[0]
    for i in range(1, n):
        result = result * r + poly[i]
    print("The Value of the Polynomial at r = " + str(r) + " is " + str(result))

def main():
    # x4 - 4x3 + 7x2 - 5x + 2 at r = 3
    poly = [1, -4, 7, -5, 2]
    r = 3
    n = len(poly)
    horner(poly, n, r)

main()