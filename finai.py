import openai
import streamlit as st

key = "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"
openai.api_key = key

messages = [{"role": "system", "content": "Do a commentary on the provided data. Here are some basic rules for organizing transaction data:1. Organize the transaction data by credit and debit activities separately.2. For each type of transaction (International Wires, Domestic Wires, ACH Deposits, etc.), provide a summary of the total number and value of transactions.3. Identify the top 3 counterparties by value for each type of transaction, and include the FATF country risk rating for international transactions.4. For ACH and wire transactions, provide a minimum of 10 counterparty samples or 10% of the total number of transactions, whichever is less.5. For Cash and Check transactions, provide a range of deposit or withdrawal amounts.6. For Internal Transfers, identify the originating and destination accounts.In addition to these rules, please include the FATF country risk ratings for all countries involved in international transactions. The ratings are as follows:- Low Risk Countries: [list of countries]- Moderate Risk Countries: [list of countries]- High Risk Countries: [list of countries]Please adjust these rules as needed to get good examples.DONOT consider the NaN values."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply