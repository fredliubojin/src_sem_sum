import os
import openai
import json
import unittest
import re
import ijson

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the prompt for the GPT-3 API
def get_user_message(file_path, file_content):
    return f"""
    Below is the content of a source file (path={file_path}) :

    ```{file_content}```.

    Based on the content of the source file, please generate a JSON file that
    1: provide a one line descriptoin for explaining general purpose of the file,
    2: list all imported symbols,
    3: provide one line description for all exported symbols.
    The result should be in JSON format as specified below, without any additional description of the response:

    ```
    {{
        "path": path_of_the_file,
        "file_purpose": purpose_of_the_file,
        "imported_symbols": ["import_symbol1", "import_symbol2", ...],
        "exported_symbols": [
            {{"exported_symbola": "description_of_symbola"}},
            {{"exported_symbolb": "description_of_symbolb"}}
        ]
    }}
    ```
    """

def get_prompt_messages(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    messages = [
            {
                "role": "system",
                "content": "You are a sophisticated, accurate, and modern AI programming assistant that understands code base in java, python, javascript, typescript, golang, rust, c and c++"
            },
            {
                "role": "user",
                "content":get_user_message(file_path, file_content)
            }
        ]
    return messages

def parse_response(raw_response):
    '''
    parsing raw json out of the response and convert to python object
    TODO: more robust parsing, potentially with JSON schema
    '''
    start = raw_response.find('{')
    if start == -1:
        return {}
    # Find the end of the first JSON object by matching brackets
    end = start
    brackets = 0
    while end < len(raw_response):
        if raw_response[end] == '{':
            brackets += 1
        elif raw_response[end] == '}':
            brackets -= 1
        if brackets == 0:
            break
        end += 1
    return json.loads(raw_response[start:end+1])

def get_summary_response(file_path):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=get_prompt_messages(file_path),
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

def process_files(directory, results):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            results[file_path] = get_summary_response(file_path)
        elif os.path.isdir(file_path):
            process_files(file_path, results)

def get_results(directory):
    results = {}
    process_files(directory, results)
    return results

def get_json_results(directory):
    results = get_results(directory)
    return json.dumps(results, indent=4)


if __name__ == '__main__':
    print(get_results("."))