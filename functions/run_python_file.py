import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs, file_path))
    valid_target_file = os.path.commonpath([abs, target_file]) == abs

    if file_path.rfind(".py") != len(file_path) - 3:
        return f'Error: "{file_path}" is not a Python file'

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    command = ["python", target_file]

    if args is not None:
        command.extend(args)

    try:
        process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        output = ""
        
        if process.returncode != 0:
            output += f"Error: executing Python file: {e}"

        if len(process.stdout) == 0 and len(process.stderr) == 0:
            output += "No output produced"
        else:
            if len(process.stdout) > 0:
                output += f'STDOUT: {process.stdout}'
            if len(process.stderr) > 0:
                output += f'STDERR: {process.stderr}'

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"