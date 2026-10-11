import Classes
from colorama import Fore, Style, init
init()

def main():
    rectangle = Classes.Rectangle(18, 18, "синий")
    print(Fore.BLUE + Style.BRIGHT + rectangle.get_name() + Style.RESET_ALL)
    print(rectangle)

    circle = Classes.Circle(18, "зелёный")
    print(Fore.GREEN + Style.BRIGHT + circle.get_name() + Style.RESET_ALL)
    print(circle)

    square = Classes.Square(18, "красный")
    print(Fore.RED + Style.BRIGHT + square.get_name() + Style.RESET_ALL)
    print(square)

if __name__ == '__main__':
    main()
