"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
20/03/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: definitions of different types of inputs (text, url, chatgpt and file)
"""
#region Imports
import os.path
import requests
import json
from openai import OpenAI
#endregion

#region Functions
def get_gpt_api_key():
    if os.path.exists('gptapikey'):
        with open("gptapikey", 'r') as apikey:
            key = str(apikey.read())
            return key
    else:
        print("Couldn't find 'gptapikey' file with the OpenAI API key, please create it and add the key.")
        exit(1)
def get_input(opt):
    options = {
        '1': 'Enter text: ',
        '2': 'Enter URL: ',
        '3': 'Enter prompt: ',
        '4': 'Enter file to read: '
    }
    text = input(options[opt])
    return text

def get_data_from_server():
    url = 'https://api.api-ninjas.com/v1/dadjokes?limit=1'
    HEADERS = {
        'X-Api-Key': '5pr0Fq0BXisIc/TPmhtAmw==e6G2nAq8szLFLdGr'
    }
    r = requests.get(url, headers=HEADERS)
    if r.status_code == requests.codes.ok:
        text = r.json()
        text = text[0]['joke']
    else:
        print(f'Error {r.status_code}')
        exit(1)
    return text

def get_data_from_chatgpt(opt):
    try:
        apikey = get_gpt_api_key()
        client = OpenAI(api_key=apikey)
        ENGINE = "gpt-3.5-turbo-instruct"
        ANSWER_QUANTITY = 1
        MAX_TOKENS = 150
        query = get_input(opt)
        answer = client.chat.completions.create(
            model=ENGINE,
            n=ANSWER_QUANTITY,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": query}
            ]
        )
    except Exception as e:
        return e
    return answer

def get_data_from_file(opt):
    file = get_input(opt)
    if os.path.exists(file):
        with open(file, 'r') as file:
            text = file.read()
    else:
        print(f'File "{file}" not found.')
        exit(1)
    return text
#endregion
