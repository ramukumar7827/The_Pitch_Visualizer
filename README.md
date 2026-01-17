# Pitch Visualizer

Pitch Visualizer is an AI-powered web application that converts a short narrative story into a multi-panel visual storyboard.  
It intelligently breaks a story into key moments, generates detailed image prompts using a Large Language Model (LLM), and renders corresponding images using a text-to-image diffusion model.

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

### Backend
- Python
- Flask
- LangChain
- Hugging Face Inference API
- HTML
- Bootstrap
- jQuery

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

1.Prompt Engineering

The input story is sent to an LLM (DeepSeek-V3.2) with a carefully designed prompt that instructs the model to:

Decompose the story into narrative beats

Output a simple list of image generation prompts

Step 3: Output Extraction & Validation

Instead of enforcing rigid JSON schemas, the system:

Extracts only the structured list using regex

Converts it into Python-native objects

Validates required keys (prompt)

This approach significantly improves reliability in real-world LLM usage.

Step 2: Image Generation

Each prompt is sent to Stable Diffusion XL (SDXL) via the Hugging Face Inference API.
Generated images are stored locally and returned to the frontend.

