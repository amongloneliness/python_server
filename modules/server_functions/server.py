from modules.server_functions.server_auth import server_auth
from modules.server_functions.server_list import server_list
from modules.server_functions.server_info import server_info
from modules.server_functions.server_retr import server_retr
from modules.server_functions.server_exit import server_exit
from modules.server_functions.server_help import server_help
from modules.server_functions.server_fail import server_fail
from modules.server_functions.server_auth_fail import server_auth_fail
from modules.server_functions.is_auth import is_auth
from modules.server_functions.defines import *


# Обработка запроса пользователя.
def server(command):
    # Проверка количества атрибутов.
    if len(command) == 0:
        return server_fail()

    # Результат проверки активации аккаунта.
    active_account = is_auth()

    # Справка по командам.
    if command[0] == SERVER_HELP:
        return server_help()

    # Вход в учетную запись
    elif command[0] == SERVER_AUTH:
        return server_auth(command)

    # Выход из учетной записи
    elif command[0] == SERVER_EXIT:
        return server_exit()

    # Вывод списка файлов в каталоге.
    elif command[0] == SERVER_LIST:
        # Проверка аккаунта.
        if active_account:
            return server_list()
        else:
            return server_auth_fail(SERVER_LIST)

    # Вывод информации о файле.
    elif command[0] == SERVER_INFO:
        # Проверка аккаунта.
        if active_account:
            return server_info(command)
        else:
            return server_auth_fail(SERVER_INFO)

    # Перенос файлов в рабочий каталог.
    elif command[0] == SERVER_RETR:
        # Проверка аккаунта.
        if active_account:
            return server_retr(command)
        else:
            return server_auth_fail(SERVER_RETR)
    else:
        return f'неверный атрибут «{command[0]}»\n' \
               f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'

    return ''
