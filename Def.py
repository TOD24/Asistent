import subprocess
import os


def Programs(file_puth):  # функция запуска программ по пути
    try:
        subprocess.Popen(file_puth, shell=True)
        print(f"Программа {file_puth} запущенна")
    except Exception as e:
        print(f"ошибка при запуске программы {e}")


def sustem(comand):
    try:
        if "off" in comand:
            os.system("shutdown /s /t 0")
        elif "reboot" in comand:
            os.system("shutdown /r /t 0")
        elif "h" in comand:
            os.system("shutdown /h /t 0")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
