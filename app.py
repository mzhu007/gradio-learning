
import gradio as gr


def greet(name):
    name = name.strip()

    if not name:
        return "Please enter your name."

    return f"Hello, {name}! Welcome to Gradio."


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(
        label="Your name",
        placeholder="Enter your name..."
    ),
    outputs=gr.Textbox(label="Greeting"),
    title="My First Gradio App",
    description="A simple interactive Python application."
)

if __name__ == "__main__":
    demo.launch()
