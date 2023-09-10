import pandas as pd
import streamlit as st
import json

def show_tac():
    st.title("_Transaction Analysis Calculations_ ➕➗")

    st.markdown("---")

    uploaded_file = st.sidebar.file_uploader('Upload a CSV file', type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Number of different transactions using transaction description
        num_unique_transactions = df['Transaction Description'].nunique()

        # Number of different counterparties
        num_unique_counterparties = df['Counterparty'].nunique()

        # Total Amount $
        total_amount = df['Amount $'].sum()

        # Number of credit and debit transactions and their totals
        credit_transactions = df[df['Credit/Debit'] == 'Credit']
        debit_transactions = df[df['Credit/Debit'] == 'Debit']
        total_credit_amount = credit_transactions['Amount $'].sum()
        total_debit_amount = debit_transactions['Amount $'].sum()
        num_credit_transactions = len(credit_transactions)
        num_debit_transactions = len(debit_transactions)

        # Different number of countries
        num_countries = df['Country'].nunique()

        # Unique account numbers in the dataset
        unique_account_numbers = df['Account'].unique()

        # FATF country risk ratings
        fatf_country_ratings = df[['Country', 'FATF Country Risk Rating']].drop_duplicates()

        # Group by transaction description and calculate totals
        transaction_description_totals = df.groupby('Transaction Description')['Amount $'].sum()

        # Group by counterparty and calculate totals
        counterparty_totals = df.groupby('Counterparty')['Amount $'].sum()

        # Group by account and transaction type (credit/debit) and calculate totals
        account_transaction_type_totals = df.groupby(['Account', 'Credit/Debit'])['Amount $'].sum().unstack()

        # Calculate average transaction amount
        average_transaction_amount = total_amount / (num_credit_transactions + num_debit_transactions)

        # Group by country and calculate total transaction amount per country
        country_total_amount = df.groupby('Country')['Amount $'].sum()

        # Calculate transaction count by country and FATF rating
        country_fatf_transaction_count = df.groupby(['Country', 'FATF Country Risk Rating'])['Transaction Date'].count()

        # Calculate average transaction amount by transaction description
        average_amount_by_transaction = df.groupby('Transaction Description')['Amount $'].mean()

        # Calculate ACH Deposits information
        ach_deposits = df[df['Transaction Description'] == 'ACH In']
        num_ach_deposit_transactions = len(ach_deposits)
        ach_deposit_total_amount = ach_deposits['Amount $'].sum()
        ach_deposit_counterparty_info = ach_deposits.groupby('Counterparty')['Amount $'].sum()

        # Print the calculated information
        col1,col2 = st.columns(2)
        with col1:
            st.write("Number of Unique Transactions:", num_unique_transactions)
            st.write("Number of Unique Counterparties:", num_unique_counterparties)
            st.write("Total Amount $:", total_amount)
            st.write("Number of Credit Transactions:", num_credit_transactions)
            st.write("Total Credit Amount:", total_credit_amount)
            st.write("Number of Debit Transactions:", num_debit_transactions)
            st.write("Total Debit Amount:", total_debit_amount)
            st.write("Different Number of Countries:", num_countries)
            st.write("Account Numbers Analyzed:", unique_account_numbers)
            st.write("FATF Country Risk Ratings:\n", fatf_country_ratings)

            st.write("\nTransaction Description Totals:")
            st.write(transaction_description_totals)

            st.write("\nCounterparty Totals:")
            st.write(counterparty_totals)
        with col2:
            st.write("\nAccount Transaction Type Totals:")
            st.write(account_transaction_type_totals)

            st.write("\nAverage Transaction Amount:", average_transaction_amount)

            st.write("\nCountry Total Amount:")
            st.write(country_total_amount)

            st.write("\nCountry FATF Transaction Count:")
            st.write(country_fatf_transaction_count)

            st.write("\nAverage Transaction Amount by Transaction Description:")
            st.write(average_amount_by_transaction)

            st.write("\nACH Deposits:", num_ach_deposit_transactions, "transactions totaling $", ach_deposit_total_amount, "primarily from:")
            for counterparty, amount in ach_deposit_counterparty_info.items():
                st.write(f"{counterparty}: {len(ach_deposits[ach_deposits['Counterparty'] == counterparty])} transactions, ${amount}")