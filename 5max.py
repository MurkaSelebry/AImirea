def main(y, x, z):
    sum = 0
    n = len(y)
    y = [0] + y
    z = [0] + z
    x = [0] + x
    for i in range(1, n + 1):
        a = z[i] ** 2 + x[i] ** 3
        b = 99 * y[n + 1 - i]
        sum += 63 * (a + b) ** 4
    return 84 * sum
