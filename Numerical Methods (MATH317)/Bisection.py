def f(x):
    return pow(x, 3) - 3 * x + 1

def sign(nm):
    return -1 if nm < 0 else 1

def Bisection(f, a, b, mmax, e):
    fa = f(a)
    fb = f(b)

    if sign(fa) == sign(fb):
        print("\t", a, "\t", b, "\t", fa, "\t", fb, "\t")
        print("function has same signs at a and b")

    error = b - a

    for n in range(mmax):
        error = error / 2
        c = a + error
        fc = f(c)
        print(n, "\t", c, "\t\t\t\t", fc, "\t\t\t\t", error,"\t\t\t\t")
        if abs(error) < e:
            print("convergence")
        if sign(fa) != sign(fc):
            b = c
            fb = fc
        else:
            a = c
            fa = fc

if __name__ == "__main__":
    mmax = 20
    e = 0.5 * 0.000001
    a = 0
    b = 1
    Bisection(f, a, b, mmax, e)