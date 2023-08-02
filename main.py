import streamlit as st
import pandas as pd
import openai

def show_tar():
        # Add the text fields
        col1,col2 = st.columns(2)
        with col1:
        client_name = st.text_input("Client Name")
        naics_code = st.text_input("NAICS Code")
        acc_no = st.text_input("Account Number (Use ',' for multiple accounts)")
        review_period_start = st.date_input("Review Period Start", value=None)
        review_period_end = st.date_input("Review Period End", value=None)
        wire_counterparty_options = st.multiselect("Number of Wire Counterparties", options=["Top 10", "Top 20", "10%", "20%"])
        with col2:
        ach_counterparty_options = st.multiselect("Number of ACH Counterparties", options=["Top 10", "Top 20", "10%", "20%"])
        authorized_signers = st.text_input("Authorized Signers (Use ',' for multiple)")
        beneficial_owners = st.text_input("Beneficial Owners (Use ',' for multiple)")
        control_person = st.text_input("Control Person")
        attorney = st.text_input("Power of Attorney")
        business_description = st.text_area("Business purpose/model description")
        
        
        # Add the checkboxes for selecting the number of counterparties
        st.markdown("---")
        
        uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
        
        if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        df['Amount $'] = df['Amount $'].astype(str)
        
        # Calculate the total credit and debit amounts and transactions
        credit_transactions = df[df['Credit/Debit'] == 'Credit']
        total_credit_amount = credit_transactions['Amount $'].str.replace(',', '').str.replace('$', '').astype(float).sum()
        total_credit_transactions = credit_transactions.shape[0]
        
        debit_transactions = df[df['Credit/Debit'] == 'Debit']
        total_debit_amount = debit_transactions['Amount $'].str.replace(',', '').str.replace('$', '').astype(float).sum()
        total_debit_transactions = debit_transactions.shape[0]
        
        # Display the total credit and debit amounts and transactions
        # st.markdown(f"**Credits:** {total_credit_transactions} transactions totaling ${total_credit_amount:,.2f}")
        # st.markdown(f"**Debits:** {total_debit_transactions} transactions totaling ${total_debit_amount:,.2f}")
        
        # Display the DataFrame
        st.dataframe(df)
        
        # Convert DataFrame to a string representation
        text = df.to_string(index=False)
        
        st.write(f"Token: {len(text)}")
        
        # Truncate the string to a reasonable length for GPT
        # text = text[:4096]
        
        # Display the truncated string
        # st.text(text)
        print(text)
        
        if st.button('TRANSACTION ANALYSIS REPORT'):
            prompt = 'prompt_TAR.txt'
            with open(prompt, 'r') as file:
                content = file.read()
        
            # Modify the prompt to include the new text fields and counterparty options
            TAR_intro = f"FINCOMPLYAI TRANSACTION ANALYSIS REPORT:\n\nClient Name: {client_name}\nNAICS Code: {naics_code}\nReview Period: {review_period_start} to {review_period_end}\n"
            prompt_text = f"{content}\n\nBusiness purpose/model description: {business_description}\nWire Counterparties: {wire_counterparty_options}\nACH Counterparties: {ach_counterparty_options}\n\nCredits: {total_credit_transactions} transactions totaling ${total_credit_amount:,.2f}\nDebits: {total_debit_transactions} transactions totaling ${total_debit_amount:,.2f}"
        
            messages = [{"role": "system", "content": f"Generate a transaction analysis report based on the provided CSV file. Use the following format: \n{prompt_text}"}]
        
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
            overall_tran = f"\nOVERALL TRANSACTIONS: \nCredits: {total_credit_transactions} transactions totaling ${total_credit_amount:,.2f}\nDebits: {total_debit_transactions} transactions totaling ${total_debit_amount:,.2f}"
            st.text_area('FinComplyAI:', value=f'{TAR_intro}\n{overall_tran}\n\n{response}', height=150, max_chars=None, key=None)
        
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
