# Gorilla LLM Demo

This is a quickstarter project to get started quickly with Gorilla LLM.

## How to run

1. Install the requirements

     ```pip install -r requirements.txt```

2. Run the app

    ```streamlit run app.py```
3. In the opened demo page, write a prompt. e.g. "I want to generate embeddings for a simple python program."
The Gorilla LLM will create a python file (`generated_code_gorilla_*.py`) with correct API call. Our subprocess will create the embeddings by running the python code.
