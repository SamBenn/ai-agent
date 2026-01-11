from google.genai import types

from functions.call_function import call_function

def call_llm(client, messages, config, args):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, 
                                              config=config)
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

    if response.candidates is not None and len(response.candidates) > 0:
        for candidate in response.candidates:
            messages.append(candidate.content)
    
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

            messages.append(types.Content(role="user", parts=func_call_result.parts))

    return response