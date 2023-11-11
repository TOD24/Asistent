import socket
import pickle
import psutil
import colorama

colorama.init()

# отправляет информацию на сервер
def send_data_to_ip(data_to_send, target_ip, target_port):
    s = socket.socket()

    try:
        s.connect((target_ip, target_port))
        s.sendall(pickle.dumps(data_to_send))
    except Exception as e:
        print(f"Ошибка при отправке данных: {e}")
    finally:
        s.close()

# Получает информацию о дисках
def get_free_space(drive_letter='f:'):
    try:
        partition = [p for p in psutil.disk_partitions(all=True) if p.device.startswith(drive_letter)][0]
        usage = psutil.disk_usage(partition.mountpoint)
        #return f"{drive_letter} свободно: {usage.free / (1024 ** 3):.2f} GB, использовано: {usage.percent}%"
        return drive_letter, usage
    except IndexError:
        return f"Диск {drive_letter} не найден."
    
# Получение данных
# Процессор
cpu = psutil.cpu_percent(interval=1)
# Оперативная память
memory = psutil.virtual_memory()
нагрузка_на_память = round(memory.total / (1024 ** 3), 2)
занятая_память = round(memory.used / (1024 ** 3), 2)
свободная_память = round(memory.available / (1024 ** 3), 2)
# Жесткий диск
drive_latter, usage = get_free_space('C:')


# Запись данных в словарь
text = {
    "нагрузка процессора": {"value": f"{colorama.Fore.RED}{cpu}%{colorama.Style.RESET_ALL}    ", "x": 22, "y": 3},
    "нагрузка на память": {"value": f"{colorama.Fore.GREEN}{memory.percent}%{colorama.Style.RESET_ALL}    ", "x": 21, "y": 4},
    "общее количество памяти": {"value": f"{colorama.Fore.CYAN}{нагрузка_на_память} ГБ{colorama.Style.RESET_ALL}    ", "x": 26, "y": 5},
    "занятая память": {"value": f"{colorama.Fore.YELLOW}{занятая_память} ГБ{colorama.Style.RESET_ALL}    ", "x": 17, "y": 6},
    "свободная память": {"value": f"{colorama.Fore.BLUE}{свободная_память} ГБ{colorama.Style.RESET_ALL}    ", "x": 19, "y": 7},
    "диск": {"value": f"{colorama.Fore.MAGENTA}{drive_latter}{colorama.Style.RESET_ALL}    ", "x": 7, "y": 8},
    "общий объем диска": {"value": f"{colorama.Fore.WHITE}{usage.total / (1024 ** 3):.2f} GB{colorama.Style.RESET_ALL}    ", "x": 20, "y": 9},
    "свободно": {"value": f"{colorama.Fore.GREEN}{usage.free / (1024 ** 3):.2f} GB{colorama.Style.RESET_ALL}    ", "x": 11, "y": 10},
    "занято": {"value": f"{colorama.Fore.RED}{usage.used / (1024 ** 3):.2f} GB{colorama.Style.RESET_ALL}    ", "x": 9, "y": 11},
    "Использованно": {"value": f"{colorama.Fore.YELLOW}{usage.percent}%{colorama.Style.RESET_ALL}    ", "x": 15, "y": 12}
}

# Преднастройки сервера
target_ip = '192.168.1.77'  # Укажите нужный IP-адрес сервера
target_port = 12345

# Вызов функции для отправки информации на сервер
send_data_to_ip(text, target_ip, target_port)

