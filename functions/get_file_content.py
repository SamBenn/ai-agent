import os

def get_file_content(working_directory, file_path):
    abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs, file_path))
    valid_target_file = os.path.commonpath([abs, target_file]) == abs

    if not valid_target_file:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isdir(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    pass