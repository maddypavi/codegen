import gradio as gr
import google.generativeai as gen
 

gen.configure(api_key='AIzaSyBSbkbzOzuCPzTTwJyzsF2DYxeq3uU_NJk')
 
models = [m for m in gen.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name if models else None
 
def translate_text(prompt):
    if model:
        completion = gen.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.1,
            max_output_tokens=300,
        )
        response = completion.result
        return response
    else:
        return "Not Found"



with gr.Blocks() as iface:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    result_btn = gr.Button("result")
    result_btn.click(fn=translate_text, inputs=name, outputs=output, api_name="submit")

iface.launch(share=True)