import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def input_data():
    # Введення кількості точок
    n = int(input("Enter the number of known points: "))

    # Введення значень X та Y
    XX = []
    YY = []

    print("Enter values for X (known points):")
    for i in range(n):
        x_value = float(input(f"X[{i}]: "))
        XX.append(x_value)

    print("Enter values for Y (known points):")
    for i in range(n):
        y_value = float(input(f"Y[{i}]: "))
        YY.append(y_value)

    return XX, YY


def output_table(XX, YY):
    # Виведення таблиці значень функції
    print("\nTable of values of a function:")
    print("X: ", end="")
    for x in XX:
        print(f"{x:7.3f}|", end="")
    print()

    print("Y: ", end="")
    for y in YY:
        print(f"{y:7.3f}|", end="")
    print()


def lagrange_interpolation(XX, YY):
    # Символічна змінна для інтерполяційного багаточлена
    x = sp.Symbol('x')

    n = len(XX)

    # Обчислення інтерполяційного багаточлена L(x)
    L = 0
    for i in range(n):
        term = YY[i]
        for j in range(n):
            if i != j:
                term *= (x - XX[j]) / (XX[i] - XX[j])
        L += term

    # Спрощення багаточлена
    L_simplified = sp.simplify(L)

    # Виведення формули інтерполяційної функції
    print("\nThe interpolation polynomial L(x) is:")
    print(L_simplified)

    # Функція для обчислення значень багаточлена
    L_func = sp.lambdify(x, L_simplified, 'numpy')

    return L_simplified, L_func


def interpolate_points(L_simplified, x):
    # Введення кількості точок для інтерполяції
    m = int(input("\nEnter the number of points to interpolate: "))
    for i in range(m):
        r = float(input(f"\nEnter value X[{i}] to interpolate: "))

        y_value = L_simplified.subs(x, r)

        print(f"For X = {r:.1f}, Y = {y_value:.3f}")


def plot_graph(L_func, XX, YY):
    # Побудова графіка інтерполяційного багаточлена
    x_vals = np.linspace(min(XX) - 1, max(XX) + 1, 500)
    y_vals = L_func(x_vals)

    plt.plot(x_vals, y_vals, label='Lagrange Polynomial', color='purple')
    plt.scatter(XX, YY, color='fuchsia', label='Given Points')

    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')

    plt.title('Lagrange Interpolation Polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    XX, YY = input_data()
    output_table(XX, YY)

    L_simplified, L_func = lagrange_interpolation(XX, YY)

    x = sp.Symbol('x')
    interpolate_points(L_simplified, x)

    plot_graph(L_func, XX, YY)


if __name__ == "__main__":
    main()
