from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                ),
            },
        ),
    )

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Retrieves the content of a specified file relative to the working directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to file, relative to the working directory",
                ),
            },
        ),
    )

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a specified python file relative to the working directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to file, relative to the working directory",
                ),
                "args": types.Schema(
                    type = types.Type.OBJECT,
                    description="Arguments for specified python file (default is None)"
                )
            },
        ),
    )

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes to a specified file, creates any non-existing directories necessary",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to file, relative to the working directory",
                ),
                "content": types.Schema(
                    type = types.Type.STRING,
                    description="Intended content of the specified file"
                )
            },
        ),
    )