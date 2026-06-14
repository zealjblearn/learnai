import gradio as gr
from ollama import chat

def generate_response(message, history):
    
    messages = []
    messages.extend(history)
    # for user_msg, assistant_msg in history:
    #     messages.append({"role": "user", "content": user_msg})
    #     messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": message})

    response = ""

    stream = chat(
        model="llama3.2",
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        response += chunk["message"]["content"]
        yield response

# chatbot = generate_response("what is the gold price", [])
# print(next(chatbot))
# print(next(chatbot))
# print(next(chatbot))

demo = gr.ChatInterface(fn=generate_response, title="Bharathi ChatBot")
demo.launch()