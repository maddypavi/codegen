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
            temperature=0.8,
            max_output_tokens=500,
        )
        response = completion.result
        return response
    else:
        return "Not Found"

iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(placeholder="Enter text here..."), 
    outputs=gr.Textbox(),  
    live=True,  
    title="CODE-GEN",  
    description="Enter text and see the processed result.",  
)

# Launch the interface
iface.launch(share=True)