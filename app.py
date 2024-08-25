import os
import sys
import datetime

# Определение пути. Закомментируйте следующую строку, если хотите использовать корневой каталог.
# path = '/ваш/путь/к/каталогу'
path = os.path.expanduser('~')  # Замените на '/mnt', если используете монтирование

def count_files(path):
    return sum(os.path.isfile(os.path.join(path, name)) for name in os.listdir(path))

def top_10_files_by_size(path):
    files = [(f, os.path.getsize(os.path.join(path, f))) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:10]

if __name__ == "__main__":
    # Получение имени из аргументов командной строки
    name = sys.argv[1] if len(sys.argv) > 1 else "Гость"
    
    # Вывод приветствия с текущей датой и временем
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Привет, {name}! Текущая дата и время: {current_time}")
    
    # Подсчет файлов
    file_count = count_files(path)
    print(f"Общее количество файлов в пути '{path}': {file_count}")
    
    # Вывод топ-10 файлов по размеру
    top_files = top_10_files_by_size(path)
    print("Топ-10 файлов по размеру (в Кб):")
    for file, size in top_files:
        print(f"{file} - {size / 1024:.2f} Кб")
