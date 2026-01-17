from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate(
    template="""
    The Pitch Visualizer," that ingests a block of narrative text, deconstructs it into key moments, and programmatically generates a multi-panel visual storyboard. The core of this challenge lies in the intelligent translation of textual concepts into effective, descriptive prompts for an AI image generation model.
    Your task to covert input into visual step by step prompt such that if i give individual panal to TTI it will generate correlated image.
    OUTPUT FORMAT:[
    {{
        "panel": 1,
        "caption": "short narrative beat",
        "prompt": "detailed image generation prompt"
    }}
    ]
    current input:{input}


    """,
    input_variables=['input'],
    validate_template=True,

    )