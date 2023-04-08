from os import remove
from os.path import exists
from modules.server_functions.defines import *


# Завершение работы.
def server_exit():
    # Проверка наличия файла аутефикации.
    if exists(FILE_AUTH):
        remove(FILE_AUTH)
    else:
        return 'Вы не вошли в аккаунт.\n'

    return 'Вы вышли из аккаунта.\n'

