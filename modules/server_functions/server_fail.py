from sys import argv, exit


# Обработка отсутствия аргументов.
def server_fail():
    return f'server: пропущен операнд\n' \
           f'По команде «help» можно получить дополнительную информацию.\n'
