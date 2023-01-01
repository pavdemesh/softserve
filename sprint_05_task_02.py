def solve_quadratic_equation(a, b, c):
    # do the checks first
    try:
        d = b ** 2 - 4 * a * c

        if d < 0:
            print("No solution")
            return

        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            print(f"The solution are x1={x1} and x2={x2}")
            return

        if d == 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            print(f"The solution is x1={x1}")

    except ZeroDivisionError:
        print(f"Zero Division Error")
    except TypeError:
        print("Could not convert string to float")


solve_quadratic_equation(0, 6, 9)
solve_quadratic_equation(1, 5, 6)
solve_quadratic_equation(5, 10, "3")
