import controler as ctrl, view as v

print("\033[H\033[J", end='')  # Переміщує курсор у верхній лівий кут і очищує екран

def main():
    ctrl.hello()
    while True:
        cmd = ctrl.get_cmd()
        if cmd == '':
            ctrl.wrong_command('')
            continue
        cmd, args = parse_input(cmd)
        if cmd in ('hi', 'hello', 'привіт'):
            ctrl.hello()
        elif cmd in ('quit', 'exit', 'close'):
            ctrl.quit()
        elif cmd == 'add':
            ctrl.add_contact(args)
        elif cmd == 'change':
            ctrl.change_contact(args)
        elif cmd == 'remove':
            ctrl.remove_contact(args)
        elif cmd == 'phone':
            ctrl.show_phone(args)
        elif cmd == 'all':
            ctrl.show_all()
        elif cmd == 'clrscr':
            v.clear_screen()
        elif cmd == '?':
            ctrl.help()
        else:
            ctrl.wrong_command(cmd)

def parse_input(cmd:str) -> tuple[str, list]:
    cmd = cmd.split()
    return cmd[0].lower(), [] if len(cmd) == 1 else cmd[1:]

def add_contact():
    pass

if __name__ == "__main__":
    main()