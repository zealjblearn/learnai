import gradio as gr

def say_hello(name):
    return f"Welcome to AI world!!, {name}"


# demo= gr.Interface(fn=say_hello, inputs="text", outputs="text")

txt = gr.Textbox(label="User Input", placeholder="Type here...", lines=2)

temp = gr.Slider(minimum=0.0, maximum=1.0, value=0.3, label="Temperature")

# demo= gr.Interface(fn=say_hello, inputs=[txt, temp], outputs="text")

# with gr.Blocks() as demo:
#     gr.Markdown("# LearnLessDaily Layout")
# with gr.Row():
#     inp = gr.Textbox()
#     out = gr.Textbox()

import gradio as gr

def say_hello(name, temperature):
    return f"Welcome to AI world!!, {name}. Temperature={temperature}"

with gr.Blocks() as demo:
    gr.Markdown("# My First AI App")

    txt = gr.Textbox(
        label="User Input",
        placeholder="Type here..."
    )

    temp = gr.Slider(
        minimum=0.0,
        maximum=1.0,
        value=0.3,
        label="Temperature"
    )

    output = gr.Textbox(label="Response")

    btn = gr.Button("Submit")

    btn.click(
        fn=say_hello,
        inputs=[txt, temp],
        outputs=output
    )

demo.launch()