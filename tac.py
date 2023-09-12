# import pandas as pd
# import streamlit as st
# import openai

# def show_tac():
#     st.title("_Transaction Analysis Calculations_ ➕➗")

#     st.markdown("---")

#     uploaded_file = st.sidebar.file_uploader('Upload a CSV file', type=['csv'])
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)

#         # Number of different transactions using transaction description
#         num_unique_transactions = df['Transaction Description'].nunique()

#         # Number of different counterparties
#         num_unique_counterparties = df['Counterparty'].nunique()

#         # Total Amount $
#         total_amount = df['Amount $'].sum()

#         # Number of credit and debit transactions and their totals
#         credit_transactions = df[df['Credit/Debit'] == 'Credit']
#         debit_transactions = df[df['Credit/Debit'] == 'Debit']
#         total_credit_amount = credit_transactions['Amount $'].sum()
#         total_debit_amount = debit_transactions['Amount $'].sum()
#         num_credit_transactions = len(credit_transactions)
#         num_debit_transactions = len(debit_transactions)

#         # Different number of countries
#         num_countries = df['Country'].nunique()

#         # Unique account numbers in the dataset
#         unique_account_numbers = df['Account'].unique()

#         # FATF country risk ratings
#         fatf_country_ratings = df[['Country', 'FATF Country Risk Rating']].drop_duplicates()

#         # Group by transaction description and calculate totals
#         transaction_description_totals = df.groupby('Transaction Description')['Amount $'].sum()

#         # Group by counterparty and calculate totals
#         counterparty_totals = df.groupby('Counterparty')['Amount $'].sum()

#         # Group by account and transaction type (credit/debit) and calculate totals
#         account_transaction_type_totals = df.groupby(['Account', 'Credit/Debit'])['Amount $'].sum().unstack()

#         # Calculate average transaction amount
#         average_transaction_amount = total_amount / (num_credit_transactions + num_debit_transactions)

#         # Group by country and calculate total transaction amount per country
#         country_total_amount = df.groupby('Country')['Amount $'].sum()

#         # Calculate transaction count by country and FATF rating
#         country_fatf_transaction_count = df.groupby(['Country', 'FATF Country Risk Rating'])['Transaction Date'].count()

#         # Calculate average transaction amount by transaction description
#         average_amount_by_transaction = df.groupby('Transaction Description')['Amount $'].mean()

#         # Calculate ACH Deposits information
#         ach_deposits = df[df['Transaction Description'] == 'ACH In']
#         num_ach_deposit_transactions = len(ach_deposits)
#         ach_deposit_total_amount = ach_deposits['Amount $'].sum()
#         ach_deposit_counterparty_info = ach_deposits.groupby('Counterparty')['Amount $'].sum()

#         # Print the calculated information
#         col1,col2 = st.columns(2)
#         with col1:
#             st.write("Number of Unique Transactions:", num_unique_transactions)
#             st.write("Number of Unique Counterparties:", num_unique_counterparties)
#             st.write("Total Amount $:", total_amount)
#             st.write("Number of Credit Transactions:", num_credit_transactions)
#             st.write("Total Credit Amount:", total_credit_amount)
#             st.write("Number of Debit Transactions:", num_debit_transactions)
#             st.write("Total Debit Amount:", total_debit_amount)
#             st.write("Different Number of Countries:", num_countries)
#             st.write("Account Numbers Analyzed:", unique_account_numbers)
#             st.write("FATF Country Risk Ratings:\n", fatf_country_ratings)

#             st.write("\nTransaction Description Totals:")
#             st.write(transaction_description_totals)

#             st.write("\nCounterparty Totals:")
#             st.write(counterparty_totals)
#         with col2:
#             st.write("\nAccount Transaction Type Totals:")
#             st.write(account_transaction_type_totals)

#             st.write("\nAverage Transaction Amount:", average_transaction_amount)

#             st.write("\nCountry Total Amount:")
#             st.write(country_total_amount)

#             st.write("\nCountry FATF Transaction Count:")
#             st.write(country_fatf_transaction_count)

#             st.write("\nAverage Transaction Amount by Transaction Description:")
#             st.write(average_amount_by_transaction)

#             st.write("\nACH Deposits:", num_ach_deposit_transactions, "transactions totaling $", ach_deposit_total_amount, "primarily from:")
#             for counterparty, amount in ach_deposit_counterparty_info.items():
#                 st.write(f"{counterparty}: {len(ach_deposits[ach_deposits['Counterparty'] == counterparty])} transactions, ${amount}")
            
#             if st.button('GENERATE'):
            
#                 messages = [{"role": "system", "content": f"Generate a clean format report based on the provided data."}]
            
#                 def CustomChatGPT(user_input):
#                     messages.append({"role": "user", "content": user_input})
#                     response = openai.ChatCompletion.create(
#                         model="gpt-3.5-turbo-0613",
#                         messages=messages
#                     )
#                     ChatGPT_reply = response["choices"][0]["message"]["content"]
#                     messages.append({"role": "assistant", "content": ChatGPT_reply})
#                     return ChatGPT_reply
            
#                 response = CustomChatGPT(text)
                
#                 st.text_area('FinComplyAI:', value=f'{response}', height=150, max_chars=None, key=None)
import pandas as pd
import streamlit as st
import openai

def show_tac():
    st.title("_Transaction Analysis Calculations_ ➕➗")

    st.markdown("---")
    key = st.sidebar.text_input("ENTER API KEY")
    openai.api_key = key
    uploaded_file = st.sidebar.file_uploader('Upload a CSV file', type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        num_unique_transactions = df['Transaction Description'].nunique()
        num_unique_counterparties = df['Counterparty'].nunique()
        total_amount = df['Amount $'].sum()
        credit_transactions = df[df['Credit/Debit'] == 'Credit']
        debit_transactions = df[df['Credit/Debit'] == 'Debit']
        total_credit_amount = credit_transactions['Amount $'].sum()
        total_debit_amount = debit_transactions['Amount $'].sum()
        num_credit_transactions = len(credit_transactions)
        num_debit_transactions = len(debit_transactions)
        num_countries = df['Country'].nunique()
        unique_account_numbers = df['Account'].unique()
        fatf_country_ratings = df[['Country', 'FATF Country Risk Rating']].drop_duplicates()
        transaction_description_totals = df.groupby('Transaction Description')['Amount $'].sum()
        counterparty_totals = df.groupby('Counterparty')['Amount $'].sum()
        account_transaction_type_totals = df.groupby(['Account', 'Credit/Debit'])['Amount $'].sum().unstack()
        average_transaction_amount = total_amount / (num_credit_transactions + num_debit_transactions)
        country_total_amount = df.groupby('Country')['Amount $'].sum()
        country_fatf_transaction_count = df.groupby(['Country', 'FATF Country Risk Rating'])['Transaction Date'].count()
        average_amount_by_transaction = df.groupby('Transaction Description')['Amount $'].mean()
        ach_deposits = df[df['Transaction Description'] == 'ACH In']
        num_ach_deposit_transactions = len(ach_deposits)
        ach_deposit_total_amount = ach_deposits['Amount $'].sum()
        ach_deposit_counterparty_info = ach_deposits.groupby('Counterparty')['Amount $'].sum()
        ach_payments = df[df['Transaction Description'] == 'ACH Out']
        num_ach_payments_transactions = len(ach_payments)
        ach_payments_total_amount = ach_payments['Amount $'].sum()
        ach_payments_counterparty_info = ach_payments.groupby('Counterparty')['Amount $'].sum()

        
        text = f"Number of Unique Transactions: {num_unique_transactions}\n"
        text += f"Number of Unique Counterparties: {num_unique_counterparties}\n"
        text += f"Total Amount $: {total_amount}\n"
        text += f"Number of Credit Transactions: {num_credit_transactions}\n"
        text += f"Total Credit Amount: {total_credit_amount}\n"
        text += f"Number of Debit Transactions: {num_debit_transactions}\n"
        text += f"Total Debit Amount: {total_debit_amount}\n"
        text += f"Different Number of Countries: {num_countries}\n"
        text += f"Account Numbers Analyzed: {unique_account_numbers}\n"
        text += "FATF Country Risk Ratings:\n" + fatf_country_ratings.to_string(index=False) + "\n"
        text += "\nTransaction Description Totals:\n" + transaction_description_totals.to_string() + "\n"
        text += "\nCounterparty Totals:\n" + counterparty_totals.to_string() + "\n"
        text += "\nAccount Transaction Type Totals:\n" + account_transaction_type_totals.to_string() + "\n"
        text += f"\nAverage Transaction Amount: {average_transaction_amount}\n"
        text += "\nCountry Total Amount:\n" + country_total_amount.to_string() + "\n"
        text += "\nCountry FATF Transaction Count:\n" + country_fatf_transaction_count.to_string() + "\n"
        text += "\nAverage Transaction Amount by Transaction Description:\n" + average_amount_by_transaction.to_string() + "\n"
        text += f"\nACH Deposits: {num_ach_deposit_transactions} transactions totaling ${ach_deposit_total_amount} primarily from:\n"
        for counterparty, amount in ach_deposit_counterparty_info.items():
            text += f"{counterparty}: {len(ach_deposits[ach_deposits['Counterparty'] == counterparty])} transactions, ${amount}\n"
        text += f"\nACH Payments: {num_ach_payments_transactions} transactions totaling ${ach_payments_total_amount} primarily from:\n"
        for counterparty, amount in ach_payments_counterparty_info.items():
            text += f"{counterparty}: {len(ach_payments[ach_payments['Counterparty'] == counterparty])} transactions, ${amount}\n"
        
        prompt = 'prompt_TAC.txt'
        with open(prompt, 'r') as file:
            content = file.read()
        prompt_text = f"{content}"

        # st.write(text)
        if st.button('GENERATE'):
            messages = [{"role": "system", "content": f"Generate a clean ordered report based on the provided data and the format. Perform simple AML risk analysis, and add context / natural language around the transaction activity and add industry types next to counterparty names" + prompt_text}]

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
