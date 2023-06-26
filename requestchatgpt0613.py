# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@File:requestchatgpt0613.py
@Time:2023/6/26 14:41
@Read: chatGPT0613函数调用脚本
"""
"""
curl https://api.openai.com/v1/chat/completions -u :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 -H 'Content-Type: application/json' -d '{
  "model": "gpt-3.5-turbo-0613",
  "messages": [
    {"role": "user", "content": "What is the weather like in Boston?"}
  ],
  "functions": [
    {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  ]
}'

return：  这意味着根据用户的输入，返回一个可以且即将被调用的function
{
  "id": "chatcmpl-7VaGntqq69tZQabpeTnL6T5NLt5ag",
  "object": "chat.completion",
  "created": 1687761945,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "function_call": {
          "name": "get_current_weather",
          "arguments": "{\n  \"location\": \"Boston, MA\"\n}"
        }
      },
      "finish_reason": "function_call"
    }
  ],
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 18,
    "total_tokens": 100
  }
}


"""
# process
#   1.用户查询物流   get function：call back 向用户索要订单的 function
"""
curl https://api.openai.com/v1/chat/completions -u :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 -H 'Content-Type: application/json' -d '{
  "model": "gpt-3.5-turbo-0613",
  "messages": [
    {"role": "user", "content": "请问我的订单怎么还不发货?"}
  ],
  "functions": [
    {
      "name": "ask_user_code",
      "description": "向用户索要电话号或者订单号",
      "parameters": {
        "type": "object",
        "properties": {
          
        },
        "required": ["nothing"]
      }
    }
  ]
}'
"""


"""
{
  "id": "chatcmpl-7Vcf2CZZ2oesQY6ptCMZtE3fn4Yyr",
  "object": "chat.completion",
  "created": 1687771136,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "\u60a8\u597d\uff01\u975e\u5e38\u62b1\u6b49\u60a8\u7684\u5546\u54c1\u8fd8\u6ca1\u6709\u53d1\u8d27\u3002\u8981\u4e86\u89e3\u5177\u4f53\u539f\u56e0\uff0c\u60a8\u53ef\u4ee5\u8054\u7cfb\u5356\u5bb6\u6216\u8005\u7269\u6d41\u516c\u53f8\uff0c\u63d0\u4f9b\u60a8\u7684\u8ba2\u5355\u53f7\u6216\u8005\u8054\u7cfb\u65b9\u5f0f\uff0c\u8be2\u95ee\u4ed6\u4eec\u5173\u4e8e\u53d1\u8d27\u7684\u60c5\u51b5\u3002\u4ed6\u4eec\u4f1a\u7ed9\u60a8\u63d0\u4f9b\u6700\u51c6\u786e\u7684\u7b54\u6848\u548c\u89e3\u51b3\u65b9\u6848\u3002  "
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 64,
    "completion_tokens": 84,
    "total_tokens": 148
  }
}
import sys; print('Python %s on %s' % (sys.version, sys.platform))
Python 3.9.16 (main, May 17 2023, 17:49:16) [MSC v.1916 64 bit (AMD64)] on win32

"""