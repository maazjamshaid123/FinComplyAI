import streamlit as st
import pandas as pd
import openai

st.set_page_config(page_title='FinComplyAI-Prototype', layout='wide', menu_items={
    'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
    'Report a bug': 'https://www.linkedin.com/in/maazjamshaid/',
    'About': 'by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'
})


key = "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"
openai.api_key = key

st.markdown('---')
col1,col2,col3 = st.columns(3)
with col2:
    # st.image("logo.png")
    st.title("$FinComplyAI$")
st.markdown('---')

# Create a file uploader component
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write(df)

    # Convert the DataFrame to a string of text
    text = df.to_string(index=False)

    text = text[:4097]

    if st.button('TRANSACTION ANALYSIS REPORT'):
        prompt = 'prompt_TAR.txt'
        with open(prompt, 'r') as file:
            content = file.read()

        messages = [{"role": "system", "content": f"Produce a Tranactional Analysis Report using the following instructions: {content}"}]

        def CustomChatGPT(user_input):
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply
        # Use the text as user input to GPT's API
        response = CustomChatGPT(text)

        # Display the response
        st.text_area('FinComplyAI:', value=response, height=150, max_chars=None, key=None)
