import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

logins = {
    "admin": "admin",
    "user" : "123"
}

def login(username,password):
    try:
        assert username in logins and logins[username] == password
    except AssertionError:
        return False
    else:
        return True

if login(input(Fore.CYAN + "Введіть логін: "), input(Fore.CYAN + "Введіть пароль: ")) == True:
    print(Fore.GREEN + "Вхід виконано успішно")
else:
    print(Fore.RED + "Невірне ім'я користувача або пароль")

