from openai import OpenAI
from pynput import keyboard
import time
import re

prompt_template = '你擅长学术论文翻译{title}{subject}'


def llm(url, key, model, prompt, query):
    client = OpenAI(api_key=key, base_url=url)
    messages = [{'role': 'system', 'content': prompt}, {'role': 'user', 'content': query}]
    ret = client.chat.completions.create(model=model,
                                         messages=messages,
                                         stream=True,
                                         stream_options={"include_usage": True},
                                         temperature=0)
    return ret


def copy_to_clipboard():
    control = keyboard.Controller()
    with control.pressed(keyboard.Key.ctrl):
        control.press('c')
        control.release('c')
    time.sleep(0.1)


def process_new_line(content: str) -> str:
    content = content.replace('\r\n\r\n', '\r\n')
    content = content.replace('\r\r', '\r')
    content = content.replace('\n\n', '\n')
    content = re.sub(r'(?<![.!?])\r\n', ' ', content)
    content = re.sub(r'(?<![.!?])\r', ' ', content)
    content = re.sub(r'(?<![.!?\r])\n', ' ', content)
    return content
