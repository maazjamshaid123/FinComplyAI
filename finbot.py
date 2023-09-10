import streamlit as st
import openai
import pandas as pd

def show_bot():
    key = st.sidebar.text_input("ENTER API KEY")
    openai.api_key = key

    st.title("Finbot 🤖: ") 

    uploaded_file = st. sidebar.file_uploader('Upload a CSV file', type=['csv'])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        if st.checkbox("Show Dataframe"):
        
            # Display the DataFrame
            st.dataframe(df)

        # Convert DataFrame to a string representation
        text = df.to_string(index=False)

        st.write(f"Token: {len(text)}")
        
        # Add the data to the chat history
        data_message = {"role": "system", "content": text}
        st.session_state.data_message = data_message
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi! I am Finbot"}]

    for msg in st.session_state.messages:
        if msg["role"] != "system":  # Exclude data message from chat display
            st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not key:
            st.error("Please add your OpenAI API key to continue.", icon="🚨")
            st.stop()
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Include only user input and assistant responses in the chat history
        chat_history = st.session_state.messages + [st.session_state.data_message]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)
