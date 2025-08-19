# -*- coding: utf-8 -*-
import requests
import json
import config
url = "https://api.siliconflow.cn/v1/chat/completions"
payload = {"model": "Qwen/Qwen2.5-Coder-7B-Instruct",    "messages": [{"role": "user","content": "introduce chinese people like in food"}],"stream": True, "max_tokens": 4096}
headers = {
"Authorization":config.SILICONFLOW_API_KEY,"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers,stream=True)
if response.status_code == 200: #֤���ɹ���Ӧ
    full_content = ""    
    full_reasoning_content = ""    
    for chunk in response.iter_lines():#���ж�ȡ
        if chunk: #�����Ϊ��ֵ
            chunk_str = chunk.decode('utf-8').replace('data: ', '')#���н��벢����������ϴ�������Ƴ������е�data����
            if chunk_str != "[DONE]": #����Ƿ�Ϊ���������
                chunk_data = json.loads(chunk_str) #����json���
                delta = chunk_data['choices'][0].get('delta', {})#��ȡ��������(delta)��get��key������, default������������ʱ��ֵ����������һ�����ڰ�ȫ��ȡ�ֵ��е�ֵ��һ������
               # ��ȡ���ֿ��ܵ�����
                content = delta.get('content', '')
                reasoning_content = delta.get('reasoning_content', '')
               #����������
                if content:
                    print(content, end="", flush=True)#end���⻻�У�flush������ʾ���
                    full_content += content
               #������������
                if reasoning_content:
                    print(reasoning_content, end="", flush=True)
                    full_reasoning_content += reasoning_content
else:
            print(f" fail to response:{response.status_code}")