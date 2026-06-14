import gradio as gr
from ollama import chat


def generate_response(message, history):
    messages = []

    # Convert Gradio history to Ollama format
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})

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
    

demo = gr.ChatInterface(
    fn=generate_response,
    title="Llama 3.2 Chatbot",
)

demo.launch()