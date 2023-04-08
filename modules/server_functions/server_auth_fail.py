from modules.server_functions.defines import *


# Вывод запрета вызова команды без входа в аккаунт.
def server_auth_fail(command_name):
    return f'Чтобы воспользоваться «{command_name}», войдите в аккаунт\n' \
           f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'
