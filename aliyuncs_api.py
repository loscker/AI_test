from openai import OpenAI
import config

client = OpenAI(api_key=config.aliyuncs_API_KEY,base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
response = client.chat.completions.create(
    model="qwen-max" ,
    messages=[{"role":"user","content":"目前武汉大学的舆论风波有那些"}],stream=True
)
full_content = ""
print("流式输出内容为：")
for chunk in response:
    if chunk.choices:
        full_content += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content,end="",flush=True)
