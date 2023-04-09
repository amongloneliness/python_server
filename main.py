from modules.socketserver.defines import *
from modules.server_functions.server import server
from sys import exit
import socket

# ------------------------------------------------------------- #
#                                                               #
#                      'Python Mini Server'                     #
#                                                               #
#   modules:                                                    #
#   ---------------------------------------------------------   #
#                                                               #
#       is_auth()           - проверка авторизации              #
#       server_auth()       - список файлов в каталоге          #
#       server_exit()       - выход из аккаунта                 #
#       server_fail()       - вывод ошибки неправильного        #
#                             использования.                    #
#       server_help()       - вывод справки по использованию    #
#       server_info()       - вывод информации о файле          #
#       server_list()       - вывод списка файлов каталога      #
#       server_retr()       - перемещение файла в каталог про-  #
#                             граммы                            #
#       server_auth_fail()  - вывод ошибки авторизации          #
#       server()            - обработка запроса клиента         #
#                                                               #
# ------------------------------------------------------------- #

users_queue = 3     # максимальный размер очереди
buffer_size = 4096  # размер отправляемого буфера

# Локальный сервер.
localserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localserver.bind((LOCALHOST, LOCALPORT))

# Ожидание пользователей [старт прослушивания очереди].
localserver.listen(users_queue)

while True:
    try:
        command = []

        print('Прослушивание запросов...\n')

        # Клиент.
        client, address = localserver.accept()

        # Формируем тело пакета / ответа.
        data = client.recv(buffer_size).decode('utf-8')
        data_split = data.split('\n')
        data_text = data_split.pop()

        if len(data_text) == 0:
            data = client.recv(buffer_size).decode('utf-8')
            data_split = data.split('\n')
            data_text = data_split.pop()
            
        # оставляем часть после 'v:'
        data_text = data_text[2:]

        # Вывод тела полезной нагрузки из пакета.
        print('Содержимое:')
        print('  ' + data_text + '\n')

        command = []
        data_text = data_text.split(' ')

        # Обработка лишних пробелов при парсинге.
        for item in data_text:
            if len(item) != 0:
                command.append(item)

        # Результат обработки запроса.
        result = server(command)

        # Отправление HTTP пакета клиенту.'
        client.send(HTTP_HDRS.encode('utf-8') + result.encode('utf-8'))

        # Отключаем клиента от очереди.
        client.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        localserver.close()
        print('Закрытие сервера...')
        
        exit()


