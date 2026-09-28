import math

class BiquadraticSolver:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def input_data(self, prompt):
        print(prompt)
        while True:
            try:
                coef_str = input()
                coef = float(coef_str)
                return coef
            except(IndexError, ValueError):
                print(prompt)

    def solve (self):
        result = []
        D = self.b**2 - 4*self.a*self.c
        if D == 0:
            root_y = -self.b/(2.0*self.a)
            root1 = math.sqrt(root_y)
            root2 = -math.sqrt(root_y)
            result.append(root1)
            result.append(root2)
        if D > 0:
            root_y1 = (-self.b - math.sqrt(D))/(2.0*self.a)
            root_y2 = (-self.b + math.sqrt(D))/(2.0*self.a)
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

    def get_roots(self):
        self.a = self.input_data("Введите коэффициент А")
        self.b = self.input_data("Введите коэффициент В")
        self.c = self.input_data("Введите коэффициент С")

        roots = self.solve()

        if not roots:
            print("Корней нет")
        else:
            i = 0
            while i != len(roots):
                print(f"x{1 + i} = {roots[i]}\n")
                i += 1

def main():
    solver = BiquadraticSolver()
    solver.get_roots()

if __name__ == "__main__":
    main()
