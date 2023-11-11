from fan import receive_data 

# Прослушивание данных
sender_ip, received_text = receive_data(12345)
print(f'Получено от {sender_ip}: {received_text}')