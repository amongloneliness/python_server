from os import listdir
from os.path import isfile


# Список файлов каталога программы.
def server_list():
    files = ''

    for element in listdir():
        if isfile(element):
            files += f'{element}\n'

    return f'{files}\n'
