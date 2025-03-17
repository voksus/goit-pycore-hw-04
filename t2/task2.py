from pathlib import Path

# Колірні константи для виведення тексту в консолі (для кращого вигляду виводу)
col_0 = '\033[0m'  # Стандартний
col_1 = '\033[34m' # Синій
col_2 = '\033[33m' # Жовтий
col_x = '\033[31m' # Червоний

def get_cats_info(path) -> list[dict]:
    """
    Функція приймає шлях до файлу з даними про котів
    та повертає список словників з інформацією про котів.
    """

    try:
        # Змінна для шляху до файлу
        file = Path(path)
        # Порожній список для результатів
        result = []

        if file.is_dir():   # Перевірка чи файл не є каталогом (перестраховка, виключно для Windows)
            raise IsADirectoryError()

        print(f'{col_1}Файл {col_2}{file.name}{col_1} завантажується...{col_0}')

        # Відкриваємо файл на читання
        with open(path, 'r', encoding="utf-8") as file:
            # Читаємо файл по рядках і обробляємо дані файлу
            for line in file:
                id, name, age = line.split(',')
                cat = {
                    'id':   id.strip(),     # ID кота
                    'name': name.strip(),   # Ім'я кота
                    'age':  age.strip()     # Вік кота
                }
                result.append(cat)

    except FileNotFoundError:
        print(f'{col_x}❌ Файл {col_2}{file.absolute()}{col_x} не знайдено!{col_0}')
    except IsADirectoryError:
        print(f'{col_x}❌ Шлях {col_2}{file.absolute()}{col_x} вказує на каталог, а не на файл!{col_0}')
    except PermissionError:
        print(f'{col_x}❌ Немає доступу до файлу {col_2}{file.absolute()}{col_x} !{col_0}')
    except UnicodeDecodeError:
        print(f'{col_x}❌ Файл {col_2}{file.absolute()}{col_x} містить некоректні символи!{col_0}')
    except Exception as e:
        print(f'{col_x}❌ Невідома помилка:\n{e}{col_0}')
    return result

cats_info = get_cats_info("t2/cats_data.csv")
print(cats_info)