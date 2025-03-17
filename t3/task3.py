from colorama import Fore # Використано версію 0.4.6
import sys
from pathlib import Path

# Отримуємо аргументи командного рядка
args = sys.argv[1:]

if len(args) == 0:
    print(f'{Fore.RED}❌ Помилка!{Fore.YELLOW} Введіть шлях до теки для аналізу.{Fore.RESET}')
    sys.exit()

if len(args) > 1:
    print(f'{Fore.CYAN}ℹ️ Для запуску скрипта потрібно вказати лише цільову теку. Решта аргументів ігнорується.{Fore.RESET}')

# Створюємо об'єкт класу Path цільової теки
path = Path(args[0])
print(f"{Fore.CYAN}🗨️  Аналізуємо теку {Fore.YELLOW}{path.absolute()}{Fore.CYAN}:{Fore.RESET}")


def sort_by_name(item: Path):
    """
    Функція для сортування елементів за назвою (нечутливо до регістру)
    """
    return item.name.lower()

def analyze_directory(path: Path, indent: int = 0):
    """
    Рекурсивно виводить вміст теки з кольорами та відступами
    """

    gap = ' ' * indent  # Відступ для вкладених тек та файлів
    try:
        # Розділяємо файли та теки
        directories = [item for item in path.iterdir() if item.is_dir()]
        files = [item for item in path.iterdir() if item.is_file()]

        # Сортуємо окремо (без лямбд!)
        directories.sort(key=sort_by_name)
        files.sort(key=sort_by_name)

        # Виводимо теки
        for directory in directories:
            print(f"{gap}📁{Fore.BLUE}{directory.name}/{Fore.RESET}")
            analyze_directory(directory, indent + 4)  # Рекурсивний виклик

        # Виводимо файли
        for file in files:
            print(f"{gap}📄{Fore.GREEN}{file.name}{Fore.RESET}")

    except FileNotFoundError:
        print(f'❌{Fore.RED} Помилка! Теку {Fore.YELLOW}{path.absolute()}{Fore.RED} не знайдено.{Fore.RESET}')
    except Exception as e:
        print(f'{gap}⛓️‍💥{Fore.YELLOW}{file.name}{Fore.RED} Невідома помилка: {e}{Fore.RESET}')

try:
    # Обробка ситуації, коли замість теки отримано файл
    if path.exists() and not path.is_dir():
        print(f'❌{Fore.RED} Помилка!{Fore.RESET} За вказаною адресою {Fore.YELLOW}{path.absolute()}{Fore.RESET} знайдено файл, а не теку.')
        print(f'🤔{Fore.CYAN}  Чи бажаєте перевірити батьківську теку цього файлу? (y/n): {Fore.RESET}', end='')
        resp = input()
        # За бажанням користувача можна проаналізувати теку, яка містить цей файл
        if resp.lower() in ('y', 'yes', 'так', 'так', 'tak', '+'):
            path = path.parent
            print(f'🗨️{Fore.CYAN}  Аналізуємо теку: {Fore.YELLOW}{path.absolute()}{Fore.RESET}')
        else:
            raise SystemExit()

    # Аналізуємо теку і виводимо результат
    analyze_directory(path)
except SystemExit:
    print(f'👋{Fore.YELLOW} Програму дочасно завершено. До побачення.{Fore.RESET}')
except Exception as e:
    print(f'❌{Fore.RED} Невідома помилка:\n{e}{Fore.RESET}')