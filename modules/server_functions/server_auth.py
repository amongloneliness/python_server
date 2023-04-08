from modules.server_functions.is_auth import *


# Вход в учетную запись.
def server_auth(argv):
    # Проверка наличия входа в учетную запись.
    if is_auth():
        return 'Вы уже вошли в учетную запись.\n'
    else:
        # Проверка операндов.
        if len(argv) < 3:
            return f'{argv[0]}: пропущены операнды, задающие логин и пароль\n' \
                   f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'
        elif len(argv) > 3:
            return f'{argv[0]}: получены лишние операнды, задающие логин и пароль\n' \
                   f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'
        else:
            # Открытие файла.
            file_pass = open(FILE_PASS, 'r')

            login = password = ''

            is_login = is_password = False

            for line in file_pass:
                if line[:len(line) - 1] == argv[1] and not is_login:
                    is_login = True
                    login = line[:len(line) - 1]
                elif line[:len(line) - 1] == argv[2] and not is_password:
                    is_password = True
                    password = line[:len(line) - 1]

            if is_login and is_password:
                account = open(FILE_AUTH, "w+")
                account.write(f'{login}\n')
                account.write(f'{password}\n')
                account.close()
            else:
                return 'Неверный логин или пароль.'

            # Закрытие файла.
            file_pass.close()

            return 'Вы вошли в учетную запись.\n'
