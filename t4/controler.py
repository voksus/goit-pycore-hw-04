import time, random as rnd, view as v

contacts = {}
rnd.seed(time.perf_counter())

def get_cmd() -> str:
    line_info = "Введіть команду: "
    v.prn(v.view("▶ ", '*5h') + v.view(line_info, '*h'), end=' ')
    s = input()
    print(v.go_up + v.r_cln + v.view("✓ ", "*2") + line_info + v.view(s, '-'))
    return s.strip()

def quit():
    print("До побачення 👋")
    exit(0)

def hello():
    v.lines_clean()
    options = (
        'Привіт! Чим можу допомогти?',
        'Вітаю! Я тут, щоб допомогти.',
        'Добрий день! Я до ваших послуг.',
        'Привіт, як справи?',
        'Гей, як ся маєш?',
        'Привіт-привіт! Що треба? 😉',
        'Гей! Чекаю на твої команди.',
        'Йо! Що сьогодні робимо?',
        'О, привітулі!',
        'Слухаю уважно 🤖',
        'Чим можу допомогти, друже?',
        'Вітаю! Як можу бути корисним?',
        'Добрий день! Що вас цікавить?',
        'Ласкаво прошу! Чим можу допомогти?',
        'Сервіс активовано. Що вам потрібно?',
        'Біп-буп! Робобот до ваших послуг! 🤖',
        'Завантаження ввічливості... 100% – Привіт!',
        'Хтось викликав штучний інтелект? 👀',
        'Привіт, людська істото! Що потрібно?',
        'Хей! Давай працювати! 🚀',
        'Здоровенькі були! Що треба?',
        'Поїхали! Я готовий до роботи!',
        'Готовий до виклику! Що потрібно?',
        'Я тут! Почнімо.',
        'Адресна книга відкрита! Що робимо?',
        'Запити приймаються! Чим допомогти?',
        'Когось шукаємо? Я готовий!',
        'Контакти? Команди? Що цікавить?',
        'Починаємо роботу. Введіть команду.',
    )
    print(v.view(options[rnd.randint(0, len(options) - 1)], '3'))
    v.lines +=1

def add_contact(args:list):
    if len(args) == 2:
        name, number = args[0], args[1]
        if name in contacts:
            warn(f"Такий абонент вже існує. Для заміни номеру потрібно використовувати команду {v.higlight_cmd('change')}")
            return
        contacts[name] = number
        print(f'Контакт {v.person(name)} з номером {v.phone(number)} додано.')
        v.lines +=1
    else:
        warn(f"Для внесення даних про особу команда {v.higlight_cmd('add')} повинна мати два параметри: " +\
             f"{v.person('<ім\'я>')} та {v.phone('<номер>')}\n" +\
             f"Наприклад: {v.view('add Volodymyr +380671234567', '3')}")

def change_contact(args:list):
    if len(args) == 2:
        name, number = args[0], args[1]
        if name in contacts:
            contacts[name] = number
            print(f"Номер для {v.person(name)} було змінено на {v.phone(number)}.")
            v.lines +=1
        else:
            warn(f"Такого абонента не існує. Щоб додати контакт потрібно використовувати команду {v.higlight_cmd('add')}")

def remove_contact(args:list):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            contacts.pop(name)
            print(f"Контакт на ім'я {v.person(name)} було видалено.")
            v.lines +=1
        else:
            warn(f"Такого абонента не існує.")

def show_phone(args:list):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            number = contacts[name]
            print(f"Знайдено запис для {v.person(name)} з номером {v.phone(number)}.")
        else:
            warn(f"Запису з ім'ям {v.person(name)} не знайдено.")
        v.lines +=1

def show_all():
    if len(contacts) == 0:
        warn(f'До списку контактів ще не додано жодного запису.')
        return
    keys = list(contacts.keys())
    keys.sort()
    print(f"Кількість осіб в контактах: {v.view(str(len(keys)), '*3')}")
    for name in keys:
        number = contacts[name]
        print(f' > {v.person(name)} - {v.phone(number)}')
        v.lines +=1

def help():
    print(v.view(' Ось перелік команд: ', '*0h'))

    # hi
    s = f"{v.higlight_cmd('hi')} / {v.higlight_cmd('hello')} / {v.higlight_cmd('привіт')}  "
    print(f"{s} - генерує випадкове привітання.")

    # exit
    s = f"{v.higlight_cmd('exit')} / {v.higlight_cmd('close')} / {v.higlight_cmd('quit')}  "
    print(f"{s} - вихід з програми.")

    # add
    s = f"{v.higlight_cmd('add')} {v.person('<name>')} {v.phone('<phone>')}   "
    print(f"{s} - додати до списку контактів особу і її номер. Можна використовувати лише нове ім'я.")

    # change
    s = f"{v.higlight_cmd('change')} {v.person('<name>')} {v.phone('<phone>')}"
    print(f"{s} - змінити номер особи зі списку контактів. Такий запис має існувати в списку контактів. Тож, спочатку додайте його.")

    # remove
    s = f"{v.higlight_cmd('remove')} {v.person('<name>')}        "
    print(f"{s} - видалити запис зі списку контактів. Звісно ж такий запис теж повинен існувати в списку контактів.")

    # phone
    s = f"{v.higlight_cmd('phone')} {v.person('<name>')}         "
    print(f"{s} - відобразити номер особи зі списку контактів. Також запис має існувати в списку контактів.")

    # all
    s = f"{v.higlight_cmd('all')}                  "
    print(f"{s} - відобразити всі записи осіб зі списку контактів разом з номерами.")

    # clrscr
    s = f"{v.higlight_cmd('clrscr')}               "
    print(f"{s} - очистити екран від попередніх записів.")

    # ?
    s = f"{v.higlight_cmd('?')}                    "
    print(f"{s} - викликає цю справку.")

def warn(s:str, end=None):
    v.prn(v.view(" !!! ", '0b') + ' ' + s, end=end)

def wrong_command(cmd:str):
    v.lines_clean()
    if cmd != '':
        warn(f"Невідома команда '{v.higlight_cmd(cmd)}'. Спробуйте ще раз уважніше. ", end='')
    print(f"Не знаєте команд? Тоді введіть '{v.higlight_cmd('?')}' для виклику інформації про доступні команди.")
    v.lines += 1