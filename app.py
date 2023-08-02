import streamlit as st
from intro import show_intro
from analysis import show_analysis
from wait import show_wait

st.set_page_config(page_title='FinComplyAI-Prototype', layout='wide', menu_items={
    'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
    'Report a bug': 'https://www.linkedin.com/in/maazjamshaid/',
    'About': 'by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'
})


st.sidebar.image("fincomply.png", use_column_width=True)

st.markdown('---')
key = st.sidebar.text_input("ENTER API KEY")
openai.api_key = key

# st.sidebar.markdown("---")

PAGE_DICT = {
    "What is FinComplyAI? 🧠": show_intro,
    "Transaction Analysis 💳": show_tar,
    "Negative News 📰": show_wait,
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")


#***********************************************************************************************

if page == "What is FinComplyAI? 🧠": #FIRST PAGE
    show_intro()

#***********************************************************************************************
       
elif page == "Transaction Analysis 💳": #SECOND PAGE
    show_tar()
    
#***********************************************************************************************

elif page == "Negative News 📰": #THIRD PAGE
    show_wait()

#***********************************************************************************************
