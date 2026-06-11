# print("Hello World")

from ollama import chat
print(chat)   

messages=[
    # {"role": "admin", "content": "You are a cricket expert"},
    # {"role": "user", "content": "What is the best shot to play when a bouncer is coming?"}
    {"role": "system", "content": "You are a cricket expert."},
    {"role": "user", "content": "What is best shot to play when bouncer is coming?"}
    ]
response = chat(model="llama3.2:latest", messages=messages)
print(response.message.content)

