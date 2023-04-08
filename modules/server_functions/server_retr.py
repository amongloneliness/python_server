from os import getcwd, listdir
from os.path import exists, isdir
import shutil
from modules.server_functions.defines import *


# Передача файлов указаных в строке
def server_retr(argv):
    # Проверка операндов.
    if len(argv) < 2:
        return f'{argv[0]}: пропущен операнд, задающий файл\n' \
               f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'
    else:
        for file in argv[1:]:
            # Проверка существования файла / каталога.
            if not exists(file):
                return f'{argv[0]}: невозможно отправить файл ' \
                       f'\'{file}\': Нет такого файла или каталога\n'

            # Проверка формата файла.
            elif isdir(file):
                return f'{argv[0]}: \'{file}\': Это каталог\n'

            # Копирование файла в директорию программы.
            else:
                if file in listdir():
                    return f'Каталог уже содержит файл {file}\n'
                else:
                    shutil.copy2(file, getcwd())
                    return f'Файл {file} был скопирован в каталог.\n'

    return ''
