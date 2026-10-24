
import gradio as gr

gr.close_all()

def getDetails(name, age, preference, hobbies):
    return f"Name:{name}\nAge:{age}\nSubject Preference: {preference}\nHobbies: {[h for h in hobbies]}"

demo = gr.Interface(
    fn=getDetails,
    inputs=[
        gr.Textbox(label="Name: "),
        gr.Slider(label="Age: "),
        gr.Radio(label="Subject Preference: ", choices=['C', 'C#', 'Java', 'Python']),
        gr.CheckboxGroup(label="Hobbies: ", choices=['Painting', 'Singing', 'Reading', 'Gaming'])
    ],
    outputs=[gr.Textbox()]
)

demo.launch()
