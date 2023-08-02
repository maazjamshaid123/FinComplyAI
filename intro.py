import streamlit as st

def show_intro():
    col1,col2,col3 = st.columns(3)
    with col2:
        st.title("$FinComplyAI$")
        
    st.title("_About Us_")
    st.info("FinComplyAI™ is diligently working on a groundbreaking solution that harnesses the potential of Artificial Intelligence and Machine Learning to transform intricate data sets into intelligible insights.")
    st.error("Our innovative approach aims to revolutionize the way  companies comprehend and analyze information, empowering them to make well-informed decisions with ease and efficiency. Stay tuned for the unveiling of our cutting-edge, game-changing technology.")