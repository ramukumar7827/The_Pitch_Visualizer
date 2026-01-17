from flask import Flask, render_template, jsonify, request
import nltk
from nltk.tokenize import sent_tokenize
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from huggingface_hub import InferenceClient
import os
import json
import re
load_dotenv()

app = Flask(__name__)

def prompt_engineering(input):
        
    llm1=HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V3.2",
        task='text-generation',
    
    )
    prompt=PromptTemplate(
    template="""
    The Pitch Visualizer," that ingests a block of narrative text, deconstructs it into key moments, and programmatically generates a multi-panel visual storyboard. The core of this challenge lies in the intelligent translation of textual concepts into effective, descriptive prompts for an AI image generation model.
    your task to covert input into visual step by step prompt such that if i give individual panal to TTI it will generate correlated image.
    OUTPUT FORMAT:
    [
      {{
       "prompt": "detailed image generation prompt"
      }}
    ]
    current input:{input}


    """,
    input_variables=['input'],
    validate_template=True,

    )


    model=ChatHuggingFace(llm=llm1)
    answer=model.invoke(prompt.invoke({"input":input}))
    text= re.sub(r"```json|```", "", answer.content).strip()
    match = re.search(r"\[\s*{.*}\s*\]", text, re.DOTALL)
    if not match:
            raise ValueError("No JSON array found")
    json_str=match.group(0)
    data = json.loads(json_str)
    return data



def generate_image_from_text(input,panel_id):
    print(input)

    client = InferenceClient(
        provider="nscale",
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    )

    image=client.text_to_image(
        input,
        model="stabilityai/stable-diffusion-xl-base-1.0",
    )

    os.makedirs("static/images", exist_ok=True)
    image_path = f"static/images/panel_{panel_id}.png"
    image.save(image_path)

    return image_path


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/storyboard", methods=["POST"])
def storyboard():
    story = request.json["input"]
    panels = prompt_engineering(story)

    image_paths = []
    for i, panel in enumerate(panels):
        path = generate_image_from_text(panel["prompt"], i)
        image_paths.append(path)

    return jsonify({
        "panels": panels,
        "images": image_paths
    })


   

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)




   
  