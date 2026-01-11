import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from tools import *

from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
parser = argparse.ArgumentParser("ai-agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

def main():
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    available_functions = types.Tool(
        function_declarations=[schema_get_files_info,
                               schema_get_file_content,
                               schema_run_python_file,
                               schema_write_file],
    )

    config = types.GenerateContentConfig(system_instruction=system_prompt, temperature=0, 
                                         tools=[available_functions])

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, 
                                              config=config)
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    
    print(response.text)
    if response.function_calls != None:
        for func_call in response.function_calls:
            func_call_result = call_function(func_call)
            
            if func_call_result.parts is None or func_call_result.parts == []:
                raise Exception("Function result parts are None or Empty")

            if func_call_result.parts[0].function_response.response is None:
                raise Exception("Response is None")
            
            func_results = [func_call_result.parts[0]]

            if args.verbose:
                print(f"-> {func_call_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
