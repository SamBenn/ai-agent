import os
import io

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs, file_path))
    valid_target_file = os.path.commonpath([abs, target_file]) == abs

    if not valid_target_file:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isdir(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        file = io.FileIO(target_file)
        file.read(MAX_CHARS)
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except:
        return f'Error: Thrown by standard library'