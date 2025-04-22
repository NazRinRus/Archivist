import os

source_dir = '/home/nazrinrus/PGMech'

def get_files(source_dir = os.getcwd()):

    file_list = []
    dir_list = [source_dir,]
    obj_list = os.listdir(source_dir)
    index = 0

    while len(dir_list) > 0:
        obj_list = os.listdir(dir_list[index])
        current_dir = dir_list.pop(index)
        while len(obj_list) > 0:
            if obj_list[index][0] != '.':
                current_obj = current_dir + '/' + obj_list.pop(index)
                if os.path.isfile(current_obj):
                    file_list.append(current_obj)
                elif os.path.isdir(current_obj):
                    dir_list.append(current_obj)
            else:
                obj_ignor = obj_list.pop(index)

    return file_list
