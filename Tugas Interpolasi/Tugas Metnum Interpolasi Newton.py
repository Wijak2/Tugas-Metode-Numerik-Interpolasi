def divided_diff(x, y):
    n = len(y)
    coef = [y[:]]  # Start with the y values

    for j in range(1, n):
        column = []
        for i in range(n - j):
            value = (coef[j - 1][i + 1] - coef[j - 1][i]) / (x[i + j] - x[i])
            column.append(value)
        coef.append(column)
    
    return [coef[i][0] for i in range(n)]

def newton_interpolation(x, y, xi):
    coef = divided_diff(x, y)
    n = len(coef)
    result = coef[0]
    product_term = 1

    for i in range(1, n):
        product_term *= (xi - x[i - 1])
        result += coef[i] * product_term

    return result

def main():
    x = [5, 10, 15, 20, 25, 30, 35, 40]
    y = [40, 30, 25, 40, 18, 20, 22, 15]

    xi = 20
    yi = newton_interpolation(x, y, xi)
    print(f"Interpolasi Newton di x = {xi} adalah y = {yi}")

if __name__ == "__main__":
    main()
