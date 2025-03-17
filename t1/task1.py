from pathlib import Path

# Колірні константи для виведення тексту в консолі (для кращого вигляду виводу)
col_0 = '\033[0m'  # Стандартний
col_1 = '\033[34m' # Синій
col_2 = '\033[33m' # Жовтий
col_3 = '\033[32m' # Зелений
col_x = '\033[31m' # Червоний

def total_salary(path:str) -> tuple[int, int]:
    """"
    Функція приймає шлях до файлу з зарплатами працівників.
    Повертає кортеж з загальною сумою зарплат та середньою зарплатою.
    """
    try:
        # Змінна для шляху до файлу
        file = Path(path)
        # Порожній кортеж для результатів за замовчуванням
        result = (0, 0)

        if file.is_dir():   # Перевірка чи файл не є каталогом (перестраховка, виключно для Windows)
            raise IsADirectoryError(f'Шлях {col_2}{file.absolute()}{col_x} вказує на каталог, а не на файл!{col_0}')

        print(f'Файл {col_2}{file.name}{col_0} завантажується...')

        # Відкриваємо файл на читання
        with open(path, 'r', encoding="utf-8") as file:
            # Підготовка до обробки даних
            total = 0   # Загальна сума зарплат
            average = 0 # Середня зарплата
            count = 0   # Кількість працівників

            # Читаємо файл по рядках і обробляємо дані файлу
            for line in file:
                name, salary = line.split(',')
                salary = int(salary.strip())
                print(f'{col_x}{name:>21}{col_0} - {col_1}{salary:>7,}{col_0} грн.')
                total += salary
                count += 1

            # Обчислення середньої зарплати. Якщо в файлі не знайдено даних про ЗП, то повідомляємо про це
            if count != 0:
                average = total // count
                result = (total, average)
            else:
                print(f'{col_x}У файлі {col_2}{file.absolute()}{col_x} не знайдено жодної інформації про ЗП!{col_0}')
    except FileNotFoundError:
        print(f'{col_x}❌ Файл {col_2}{file.absolute()}{col_x} не знайдено!{col_0}')
    except IsADirectoryError as e:
        print(f'{col_x}❌ {e}')
    except PermissionError:
        print(f'{col_x}❌ Немає доступу до файлу {col_2}{file.absolute()}{col_x} !{col_0}')
    except UnicodeDecodeError:
        print(f'{col_x}❌ Файл {col_2}{file.absolute()}{col_x} містить некоректні символи!{col_0}')
    except Exception as e:
        print(f'{col_x}❌ Невідома помилка:\n{e}{col_0}')
    return result

total, average = total_salary('t1/salaries.csv')
print(f'{col_3}Загальні витрати по ЗП: {col_1}{total:>7,}{col_0} грн.\n'\
      f'{col_3 + ' '*12}Середня ЗП: {col_1}{average:>7,}{col_0} грн.')