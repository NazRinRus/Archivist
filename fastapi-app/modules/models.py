import os
from datetime import datetime

class FileModel:
    def __init__(self, file_name: str):
        self.file_name = file_name
    def get_filename(self):
        return self.file_name.split('/')[-1]
    def get_filepath(self):
        return '/'.join(self.file_name.split('/')[:-1])
    def get_file_content(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"Файл {self.file_name} не найден.")
        except IOError:
            print(f"Ошибка при чтении файла {self.file_name}.")
        return file_content
    def get_updated_at(self):
        return datetime.fromtimestamp(os.path.getmtime(self.file_name)).strftime("%Y-%m-%d %H:%M:%S")
    def info(self):
        return (self.get_filename(), self.get_updated_at())

