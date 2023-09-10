import streamlit as st
import pandas as pd
import csv
import json
import openai

key = st.sidebar.text_input("ENTER API KEY")
openai.api_key = key
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

if uploaded_file is not None:
    data = []
    csv_content = uploaded_file.read()  # Read the uploaded file content

    # Decode the content to a string and split into lines
    csv_content_string = csv_content.decode('utf-8')
    csv_lines = csv_content_string.splitlines()

    # Use csv.reader to read the CSV content
    csv_reader = csv.DictReader(csv_lines)
    for row in csv_reader:
        data.append(row)

    # Convert data to JSON string
    text = json.dumps(data, indent=4)

    if st.button('GENERATE'):
            prompt = 'prompt_TAR.txt'
            with open(prompt, 'r') as file:
                content = file.read()
        
            # Modify the prompt to include the new text fields and counterparty options
            prompt_text = f"{content}"
        
            messages = [{"role": "system", "content": f"Generate a transaction analysis report based on the provided CSV file. Use the following format: \n{prompt_text}"}]
        
            def CustomChatGPT(user_input):
                messages.append({"role": "user", "content": user_input})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=messages
                )
                ChatGPT_reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": ChatGPT_reply})
                return ChatGPT_reply
        
            response = CustomChatGPT(text)
            st.text_area('FinComplyAI:', value=f'{response}', height=150, max_chars=None, key=None)
