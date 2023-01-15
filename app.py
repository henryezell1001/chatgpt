import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("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")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Act as a sports game simulation program. The user will give you a hypothetical game vs two teams and you will do your best to analyze the two teams and give the user a detailed play by play until there is a winner. the last thing you will tell the user is the final score and which team won."

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["", ""]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>ChatGPT Free</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
