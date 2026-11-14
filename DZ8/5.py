import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def process_list(*input_list):
    try:
        assert input_list.__len__() >= 3
    except AssertionError:
        return Fore.RED + "Список повинен містити принаймні 3 елементи"
    else:
        return Fore.CYAN + f"Список має {input_list.__len__()} елементів(-и)"

print(process_list(*input().split()))