import socket
import json

# Отправка данных 
def send_data(ip, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            json_data = json.dumps(data)  # Преобразование словаря в JSON-строку
            s.sendall(json_data.encode())
    except (socket.error, ConnectionRefusedError) as e:
        print(f"Ошибка при отправке данных: {e}")

# Прием данных 
def receive_data(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
            s.listen()
            print("Ждем подключения...")
            conn, addr = s.accept()
            with conn:
                print('Подключено к:', addr)
                data = conn.recv(1024)
                received_text = data.decode()
                received_data = json.loads(received_text)  # Декодирование JSON-строки в словарь
                return addr[0], received_data
    except socket.error as e:
        print(f"Ошибка при приеме данных: {e}")
        return None, None  # Возвращаем None в случае ошибки

