from modules.file_search import get_files, get_file_content, get_json_from_list
import os

def main():
    print("Hello from archivist!")


if __name__ == "__main__":
    main()
    print(get_files('/home/nazrinrus/test_source_dir'))
    print(get_file_content('/home/nazrinrus/test_source_dir/test_file3'))
    print(get_json_from_list(get_files('/home/nazrinrus/test_source_dir')))