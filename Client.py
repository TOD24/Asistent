from fan import send_data
        
# Отправка данных
text = {
    "Первое слово": "1",
    "Второе слово": "2"
}
send_data('192.168.1.77', 12345, text)

# Прослушивание данных
# sender_ip, received_text = receive_data(12345)
# print(f'Получено от {sender_ip}: {received_text}')
