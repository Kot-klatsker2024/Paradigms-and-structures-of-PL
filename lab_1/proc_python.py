import math

def get_coef(prompt):
    print(prompt)
    while True:
        try:
            coef_str = input()
            coef = float(coef_str)
            return coef

        except(IndexError, ValueError):
            print(prompt)

def get_roots(a, b, c):

    result = []

    D = b**2 - 4*a*c
    if D == 0:
        root_y = -b/(2.0*a)
        root1 = math.sqrt(root_y)
        root2 = -math.sqrt(root_y)
        result.append(root1)
        result.append(root2)
    if D > 0:
        root_y1 = (-b - math.sqrt(D))/(2.0*a)
        root_y2 = (-b + math.sqrt(D))/(2.0*a)
        if root_y1 >=0:
            root1 = math.sqrt(root_y1)
            root2 = -root1
            result.append(root1)
            result.append(root2)
        if root_y2 >= 0:
            root3 = math.sqrt(root_y2)
            root4 = -root3
            result.append(root3)
            result.append(root4)
    unique_result = list(set(result))
    return unique_result
1
-
def print_roots():
    a = get_coef("Введите коэффициент А")
    b = get_coef("Введите коэффициент В")
    c = get_coef("Введите коэффициент С")

    roots = get_roots(a, b, c)

    if not roots:
        print("Корней нет")
    else:
        i = 0
        while i != len(roots):
            print(f"x{1 + i} = {roots[i]}\n")
            i += 1



def main():
    print_roots()

if __name__ == "__main__":
    main()
