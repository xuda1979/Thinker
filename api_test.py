import requests

# 替换为你的无问芯穹 API Key
API_KEY = "sk-fpedclqqzuveyucl"

# 无问芯穹 API 请求地址
url = "https://cloud.infini-ai.com/maas/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 请求数据（使用 DeepSeek-R1 模型）
data = {
    "model": "deepseek-r1",  # R1 模型
    "messages": [
        {"role": "system", "content": "你是一个AI助手"},
        {"role": "user", "content": "请介绍一下量子计算的基本原理"}
    ],
    "stream": False  # 如需流式输出，设为 True
}

# 发送 POST 请求
response = requests.post(url, headers=headers, json=data)

# 处理响应
if response.status_code == 200:
    result = response.json()
    print("API 调用成功，返回结果：")
    print(result['choices'][0]['message']['content'])
else:
    print(f"请求失败，状态码：{response.status_code}, 错误信息：{response.text}")