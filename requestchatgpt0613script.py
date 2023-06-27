# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@File:requestchatgpt0613script.py
@Time:2023/6/26 15:23
@Read: 代码执行 call function 脚本
"""
import json
import openai
from keys import openaikeys

openai.api_key = openaikeys


def get_current_weather(location='beijing', unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    # return json.dumps(weather_info)
    # return json.dumps({'reply': "请提供您的电话号"})
    return "请提供您的电话号。"


def run_conversation():
    # Step 1: send the conversation and available functions to GPT    todo   structure： initial user question and function
    # messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    messages = [{"role": "user", "content": "为什么我的商品为何还没有发货?"}]
    functions = [
        {
            "name": "get_current_weather",
            # "description": "Get the current weather in a given location",
            "description": "当用户意图为询问商品物流信息时，调用当前方法",  # important：这里不是function的描述，这里是匹配用户意图的描述，即匹配上用户意图，就调用当前的这个function
            "parameters": {
                "type": "object",
                "properties": {
                    # "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA", },
                    # "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                # "required": ["location"],
                "required": [],
            },
        }
    ]

    # todo 知道了用户的问题以及当前问题可以调用的方案，就可以展开请求，这一步主要是确认即将调用什么function；  这是 first round request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,  # 这个参数的意义是指明当前 user ask 下，都配置了哪些function信息，例如function name/params等；但是具体的function是什么功能，在代码执行到这一步时还不清楚；
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print(type(response_message))
    # response_message['content'] = response_message['content'].decode('utf-8')
    print('response_message:', response_message)

    # Step 2: check if GPT wanted to call a function    todo chatGPT会根据用户的intent返回相应的上述传入的function信息
    if response_message.get("function_call"):
        # 所有待选择的function列表，用户的意图就是从这些相应的function list中选用
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple

        # Step 3: todo 根据用户的input intent call the 相对应的 function
        # Note: this step the JSON response may not always be valid; be sure to handle errors
        function_name = response_message["function_call"]["name"]
        # 确认当前函数name以及当前function需要的参数信息，important：这里要注意的是返回的当前function name与当前的function params相对应
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            # location=function_args.get("location"),
            # unit=function_args.get("unit"),
        )

        return function_response

        # # Step 4: send the info on the function call and function response to GPT
        # messages.append(response_message)  # extend conversation with assistant's reply
        # print("step-2: ", messages)
        # messages.append(
        #     {
        #         "role": "function",
        #         "name": function_name,
        #         "content": function_response,
        #     }
        # )  # extend conversation with function response； 追加当前的function返回的response到用户对话中，持续对话的进行
        # print('step-3: ', messages)
        # second_response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo-0613",
        #     messages=messages,
        # )  # get a new response from GPT where it can see the function response
        # return second_response


res = run_conversation()
print(res)
