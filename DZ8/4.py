import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def check_age(age):
    try:
        age = int(age)
        if age < 0 or age > 150:
            return Fore.CYAN + "ну що ти чвориш"
        else:
            assert age >= 18
    except AssertionError:
        return Fore.GREEN + "Вам має бути 18 років або більше"
    except SyntaxError:
        return Fore.YELLOW + "ти точно цифри писав?"
    except ValueError:
        return Fore.YELLOW + "ти точно цифри писав?"
    except TypeError:
        return Fore.YELLOW + "ти точно цифри писав?"
    else:
        return Fore.GREEN + "Ви можете використовувати цей сервіс"

print(check_age(input()))
