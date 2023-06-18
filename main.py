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
col1, col2, col3 = st.columns(3)
with col2:
    st.title("$FinComplyAI$")
st.markdown('---')
st.info("FinComplyAI™ is diligently working on a groundbreaking solution that harnesses the potential of Artificial Intelligence and Machine Learning to transform intricate data sets into intelligible insights. Our innovative approach aims to revolutionize the way companies comprehend and analyze information, empowering them to make well-informed decisions with ease and efficiency. Stay tuned for the unveiling of our cutting-edge, game-changing technology.")

st.markdown("---")
# Add the text fields
client_name = st.text_input("Client Name")
naics_code = st.text_input("NAICS Code")
review_period_start = st.date_input("Review Period Start", value=None)
review_period_end = st.date_input("Review Period End", value=None)
business_description = st.text_area("Business purpose/model description")
# Add the checkboxes for selecting the number of counterparties
wire_counterparty_options = st.multiselect("Number of Wire Counterparties", options=["Top 10", "Top 20", "10%", "20%"])
ach_counterparty_options = st.multiselect("Number of ACH Counterparties", options=["Top 10", "Top 20", "10%", "20%"])
st.markdown("---")

uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write(df)

    text = df.to_string(index=False)

    text = text[:4097]

    if st.button('TRANSACTION ANALYSIS REPORT'):
        prompt = 'prompt_TAR.txt'
        with open(prompt, 'r') as file:
            content = file.read()

        # Modify the prompt to include the new text fields and counterparty options
        prompt_text = f"{content}\n\nClient Name: {client_name}\nNAICS Code: {naics_code}\nReview Period: {review_period_start} to {review_period_end}\nBusiness purpose/model description: {business_description}\nWire Counterparties: {wire_counterparty_options}\nACH Counterparties: {ach_counterparty_options}"

        messages = [{"role": "system", "content": f"Produce a Transactional Analysis Report using the following instructions: {prompt_text}"}]

        def CustomChatGPT(user_input):
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply

        response = CustomChatGPT(text)

        st.text_area('FinComplyAI:', value=response, height=150, max_chars=None, key=None)

    if st.button('NEGATIVE NEWS'):
        prompt = 'prompt_NN.txt'
        with open(prompt, 'r') as file:
            content = file.read()

        # Modify the prompt to include the new text fields and counterparty options
        prompt_text = f"{content}\n\nClient Name: {client_name}\nNAICS Code: {naics_code}\nReview Period: {review_period_start} to {review_period_end}\nBusiness purpose/model description: {business_description}\nWire Counterparties: {wire_counterparty_options}\nACH Counterparties: {ach_counterparty_options}"

        messages = [{"role": "system", "content": f"Produce a Negative News Report using the following format: {prompt_text}"}]

        def CustomChatGPT(user_input):
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply

        response = CustomChatGPT(text)

        st.text_area('FinComplyAI:', value=response, height=150, max_chars=None, key=None)