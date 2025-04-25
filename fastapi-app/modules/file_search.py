import os
from models import FileModel

source_dir = '/home/nazrinrus/PGMech'

def get_files(source_dir = os.getcwd()):

    file_list = []
    dir_list = [source_dir,]
    index = 0

    while len(dir_list) > 0:
        obj_list = os.listdir(dir_list[index])
        current_dir = dir_list.pop(index)
        while len(obj_list) > 0:
            if obj_list[index][0] != '.':
                current_obj = current_dir + '/' + obj_list.pop(index)
                if os.path.isfile(current_obj):
                    file_list.append(FileModel(file_name=current_obj))
                elif os.path.isdir(current_obj):
                    dir_list.append(current_obj)
            else:
                obj_ignor = obj_list.pop(index)

    return file_list

def get_json_from_list(file_list):
    json_content = ''
    while len(file_list) > 0:
        file_name = file_list.pop(0)
        json_content = (json_content + '{"file_name": "' + file_name.file_name +
                        '", "file_content": "' + file_name.get_file_content() +
                        '", "file_updated_at": "' + file_name.get_updated_at() +'"}, ')
    return '[' + json_content + ']'