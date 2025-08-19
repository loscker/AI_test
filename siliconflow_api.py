# -*- coding: utf-8 -*-
import requests
import json
import config
url = "https://api.siliconflow.cn/v1/chat/completions"
payload = {"model": "Qwen/Qwen2.5-Coder-7B-Instruct",    "messages": [{"role": "user","content": "introduce chinese people like in food"}],"stream": True, "max_tokens": 4096}
headers = {
"Authorization":config.SILICONFLOW_API_KEY,"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers,stream=True)
if response.status_code == 200: #证明成功相应
    full_content = ""    
    full_reasoning_content = ""    
    for chunk in response.iter_lines():#逐行读取
        if chunk: #如果不为空值
            chunk_str = chunk.decode('utf-8').replace('data: ', '')#进行解码并进行数据清洗（就是移除数据中的data：）
            if chunk_str != "[DONE]": #检查是否为流结束语句
                chunk_data = json.loads(chunk_str) #解析json语句
                delta = chunk_data['choices'][0].get('delta', {})#获取增量内容(delta)，get（key（键）, default（当键不存在时的值））方法是一个用于安全获取字典中的值的一个方法
               # 提取两种可能的内容
                content = delta.get('content', '')
                reasoning_content = delta.get('reasoning_content', '')
               #处理主内容
                if content:
                    print(content, end="", flush=True)#end避免换行，flush立即显示输出
                    full_content += content
               #处理推理内容
                if reasoning_content:
                    print(reasoning_content, end="", flush=True)
                    full_reasoning_content += reasoning_content
else:
            print(f" fail to response:{response.status_code}")