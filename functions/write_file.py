import os
import io

def write_file(working_directory, file_path, content):
    abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs, file_path))
    valid_target_file = os.path.commonpath([abs, target_file]) == abs

    if not valid_target_file:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        os.makedirs(target_file[:target_file.rfind("/")], exist_ok=True)
        file = io.open(target_file, mode="w")
        file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return "Error: Thrown by standard libraries"