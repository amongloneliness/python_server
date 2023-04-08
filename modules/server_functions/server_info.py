from os.path import exists, isdir, getsize, getctime
import mimetypes as mime
import time
from modules.server_functions.defines import *


# Информация о файлах.
def server_info(argv):
    # Проверка операндов.
    if len(argv) < 2:
        return f'{argv[0]}: пропущен операнд, задающий файл\n' \
               f'По команде «{SERVER_HELP}» можно получить дополнительную информацию.\n'
    else:
        result = ''

        # Вывод файлов.
        for file in argv[1:]:
            # Вывод (mime типа / размера / даты создания) файла.
            if exists(file) and not isdir(file):
                file_type = mime.guess_type(file)[0]
                file_size = getsize(file)
                file_date = time.ctime(getctime(file))

                result += '%20s:   %13s    %10s    %15s\n' % (file, file_type, file_size, file_date)
        
        # Вывод ошибочных файлов и директорий.
        for file in argv[1:]:
            # Проверка существования файла.
            if not exists(file):
                result += f'{argv[0]}: невозможно вывести информацию о файле ' \
                       f'\'{file}\': Нет такого файла или каталога\n'

            # Проверка формата файла.
            elif isdir(file):
                result += f'{argv[0]}: \'{file}\': Это каталог\n'

    return result
