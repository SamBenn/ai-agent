import os

def get_files_info(working_directory, directory="."):
    abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs, directory))
    valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    files = os.listdir(target_dir)
    file_infos = []
    for file in files:
        file_path = os.path.normpath(os.path.join(target_dir, file))
        result = os.stat(file_path)
        file_infos.append(f'- {file}: file_size={result.st_size} bytes, is_dir={os.path.isdir(file_path)}')

    return "\n".join(file_infos)