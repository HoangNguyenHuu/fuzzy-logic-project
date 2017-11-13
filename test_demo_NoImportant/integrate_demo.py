from scipy.integrate import quad


def integrand(x, a, b):
    if x < 2:
        return a * x ** 2 + b
    else:
        return a * x + b


def result_dependency(x):
    if 0.5 < x <= 1:
        return (x - 0.5) / 0.5
    if 1 < x <= 1.5:
        return (1.5 - x) / 0.5
    return 0

m = 2
n = 1
I = quad(result_dependency, 1, 2)
print(I)
