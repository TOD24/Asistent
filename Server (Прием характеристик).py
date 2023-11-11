
import socket
import pickle
import time
import os

ip, port = '0.0.0.0', 12345
s = socket.socket()
s.bind((ip, port))
s.listen(1)


def print_system_info():
    os.system("cls")
    print("Подключено: ('0.0.0.0', 00000)")
    print("Получены данные:")
    print(f"Нагрузка процессора: {0.0}%")
    print(f"Нагрузка на память: {0.0}%")
    print(f"Общее количество памяти: {0.0} ГБ")
    print(f"Занятая память: {0.0} ГБ")
    print(f"Свободная память: {0.0} ГБ")
    print("Диск: C:")
    print(f"Общий объем диска: {0.0} GB")
    print(f"Свободно: {0.0} GB")
    print(f"Занято: {0.0} GB")
    print(f"Использовано: {0.0}%")


def printt(text,  x=0, y=0, time_ms=0.1):
    print(f"\033[{y};{x}H", end='', flush=True)
    for i in text:
        print(i, end='', flush=True)
        time.sleep(time_ms)
    print()


print_system_info()

while True:
    c, a = s.accept()

    # Принимаем данные в виде словаря
    data = b""
    while True:
        chunk = c.recv(4096)
        if not chunk:
            break
        data += chunk

    if data:
        try:
            data = pickle.loads(data)
            printt(f"Подключено: {a}",0,1,0.01)
            printt("Получены данные:",0,2,0.01)
            for key, config in data.items():
                if isinstance(config, dict):
                    value = config.get("value", "")
                    x = config.get("x", 0)
                    y = config.get("y", 0)
                    printt(value,  x, y, 0.01)
                elif isinstance(config, list):
                    for item in config:
                        printt(item)
        except pickle.UnpicklingError as e:
            printt(f"Ошибка десериализации данных: {e}")
    else:
        printt("Пустые данные получены")

    c.close()

