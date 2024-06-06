def interpolate(x, y, xi):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term = term * (xi - x[j]) / (x[i] - x[j])
        result += term

    return result

def main():
    x = [5, 10, 15, 20, 25, 30, 35, 40]
    y = [40, 30, 25, 40, 18, 20, 22, 15]

    xi = 20
    yi = interpolate(x, y, xi)
    print(f"Interpolasi Lagrange di x = {xi} adalah y = {yi}")

if __name__ == "__main__":
    main()