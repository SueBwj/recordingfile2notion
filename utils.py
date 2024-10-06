from pathlib import Path

files_dir = Path(__file__).parent.joinpath('files')
processed_dir = Path(__file__).parent.joinpath('processed_files')

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

