
import json


def load_dictionary_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
        return dictionary
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None


# Пример использования:
# Замените на имя вашего файла данных
file_name = "data_set.json"
dictionary = load_dictionary_from_file(file_name)
if dictionary:
    print(dictionary)
