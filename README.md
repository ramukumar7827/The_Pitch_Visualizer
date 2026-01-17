# Pitch Visualizer

Pitch Visualizer is an AI-powered web application that converts a short narrative story into a multi-panel visual storyboard.  
It breaks a story into key moments, generates detailed image prompts using a Large Language Model (LLM), and renders corresponding images using a text-to-image diffusion model.

This project demonstrates prompt engineering, LLM output stabilization, and end-to-end AI system integration using Flask and Hugging Face models.

---
<img width="1920" height="1080" alt="Screenshot (533)" src="https://github.com/user-attachments/assets/be4a98a9-b0a0-43ea-afd6-c3c15d67d1ca" />

## Features

- Converts narrative text into step-by-step visual prompts  
- Generates correlated storyboard images for each narrative beat  
- Displays images in a horizontal, responsive layout  
- Robust handling of LLM output variability  
- Simple local setup and execution  

---

## Tech Stack
- Python
- Flask
- LangChain
- Hugging Face Inference API
- HTML
- Bootstrap

### AI Models
- DeepSeek-V3.2 – prompt generation
- Stable Diffusion XL (SDXL) – image generation

---

## Setup and Installation

### 1. Clone the Repository
### 2. Install Dependencies
     pip install -r requirements.txt
### 3. API Key Configuration
       Create a .env file in the project root directory:
       HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
### 5. Run the Application
       python app.py



## How It Works

### Prompt Engineering

     The application sends the input story to the **DeepSeek-V3.2** language model using a carefully designed prompt.  
     The prompt instructs the model to deconstruct the narrative into key visual moments and output them as a simple, structured list of image-generation prompts.
     
     The model is explicitly guided to return only a minimal structure to improve reliability:
     json
     [
       { "prompt": "A child opens a glowing box in a dark room..." },
       { "prompt": "Light floods the room as magic spills out..." }
     ]

### Image Generation

     Each prompt is sent to Stable Diffusion XL via the Hugging Face Inference API.
     Generated images are stored locally and returned to the frontend.


