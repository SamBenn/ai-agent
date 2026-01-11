import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from tools import *

from functions.call_llm import call_llm

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
    
    response = None

    for _ in range(20):
        if response is not None and response.function_calls is None:
            break

        response = call_llm(client, messages, config, args)

if __name__ == "__main__":
    main()
