import subprocess


def Programs(file_puth):  # функция запуска программ по пути
    try:
        subprocess.Popen(file_puth, shell=True)
        print(f"Программа {file_puth} запущенна")
    except:
        print("ошибка при запуске программы")
