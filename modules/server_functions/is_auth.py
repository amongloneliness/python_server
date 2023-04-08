from modules.server_functions.defines import *
from os.path import exists


# Проверка пройденной авторизации.
def is_auth():
    check_pass = 0  # Пройденные этапы проверки [2 этапа].

    # Проверка файла аккаунта.
    if exists(FILE_AUTH):
        # Файлы сверки логина и пароля.
        file_pass = open(FILE_PASS, 'r')
        file_auth = open(FILE_AUTH, 'r')

        for line in file_pass:
            for line_auth in file_auth:
                check_pass += 1

        # Закрытие файлов.
        file_auth.close()
        file_pass.close()

    # Вывод результата проверки.
    return check_pass == 2
