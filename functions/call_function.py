from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(func_call, verbose=False):
    if verbose:
        print(f"Calling function: {func_call.name}({func_call.args})")
    else:
        print(f" - Calling function: {func_call.name}")

    func_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    func_name = func_call.name or ""

    # Func hasn't been passed in correctly or a non-mapped func is being called
    if func_call == "" or func_name not in func_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    
    args = dict(func_call.args) if func_call.args else {}

    args["working_directory"] = "./calculator"
    result = func_map[func_name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"result": result},
            )
        ],
    )