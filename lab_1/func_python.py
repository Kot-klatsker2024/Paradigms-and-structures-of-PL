import math

def calculate_biquadratic_roots(a, b, c):
    result = []
    D = b**2 - 4 * a * c

    if D == 0:
        root_y = -b / (2.0 * a)
        root1 = math.sqrt(root_y)
        root2 = -math.sqrt(root_y)
        result.append(root1)
        result.append(root2)
    elif D > 0:
        root_y1 = (-b - math.sqrt(D)) / (2.0 * a)
        root_y2 = (-b + math.sqrt(D)) / (2.0 * a)

        if root_y1 >= 0:
            result.append(math.sqrt(root_y1))
            result.append(-math.sqrt(root_y1))
        if root_y2 >= 0:
            result.append(math.sqrt(root_y2))
            result.append(-math.sqrt(root_y2))

    return list(set(result))

def safe_input_float(prompt):
    print(prompt)
    while True:
        try:
            return float(input())
        except ValueError:
            print(prompt)

def main(input_func, solver_func):

    a = input_func("Введите коэффициент А: ")
    b = input_func("Введите коэффициент В: ")
    c = input_func("Введите коэффициент С: ")

    roots = solver_func(a, b, c)

    if not roots:
        print("\nKорней нет")
    else:
        for i, root in enumerate(roots):
            print(f"x{i + 1} = {root}\n")

if __name__ == "__main__":
    main(safe_input_float, calculate_biquadratic_roots)
