import os
from openai import OpenAI

os.environ["http_proxy"] = "http://localhost:4780"
os.environ["https_proxy"] = "http://localhost:4780"


def OpenAiResponse_Sentence(content):
    client = OpenAI(
        # This is the default and can be omitted
        api_key="sk-proj-d8D3Sz7thdnXJDH6AUVLT3BlbkFJBE52sIR3V870zDD9CyEE"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )
    response_messages = chat_completion.to_dict()['choices'][0]['message']['content']
    return response_messages


def OpenAiResponse_text(sgms):
    '''

    :param file: 传入fasterwhis的字幕segments
    :return: 经过chatgpt修改的字幕segs_rm
    '''
    ct = "如下是一段关于python立体匹配算法的字幕，其中有许多谐音错误，请你在保证不修改语序的前提下，尽可能修改其中错误的谐音字段,遇到逗号,括号等词语，不要改为汉字，而是变成',''()'这样的符号，更加简洁一点“：\n"
    for sgm in sgms:
        ct += sgm[4]
    rm = OpenAiResponse_Sentence(ct)
    return rm
