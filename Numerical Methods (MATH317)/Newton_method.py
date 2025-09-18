def f(x):
    return ((x - 2) * x + 1) * x - 3 # f(x) = ((x-2)x+1)x-3

def f1(x):
    return (3 * x - 4) * x + 1 #f'(x) = (3x-4)x+1

def Newton(f, f1, x, nmax, e, g):
    fx = f(x)
    print(0, x, "\t\t\t\t\t\t", fx)

    for n in range(1, nmax+1):
        fp = f1(x)
        if abs(fp) < g:
            print("Small derivative")
        d = fx / fp
        x = x - d
        fx = f(x)
        print(n, x, "\t\t\t\t\t\t", fx)
        if abs(d) < e:
            print("Convergence")

if __name__ == "__main__":
    x = 3
    nmax = 5
    e = 0
    g = 0
    Newton(f, f1, x, nmax, e, g)