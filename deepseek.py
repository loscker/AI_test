from openai import OpenAI
import config
client = OpenAI(api_key=config.DEEPSEEK_API_KEY,
                base_url="https://api.deepseek.com")
response = client.chat.completions.create(model="deepseek-chat",
                                          messages=[{'role': 'user', "content": "世界上最好的聊天AI是那家的"}, ], 
                                           )

print(response.choices[0].message.content)