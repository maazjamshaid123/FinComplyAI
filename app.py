import streamlit as st
from intro import show_intro
from tar import show_tar
from tac import show_tac
from wait import show_wait
from viz import show_viz
from finbot import show_bot

import openai

st.set_page_config(page_title='FinComplyAI-Prototype', layout='wide', menu_items={
    'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
    'Report a bug': 'https://www.linkedin.com/in/maazjamshaid/',
    'About': 'by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'
})


st.sidebar.image("fincomply.png", use_column_width=True)

st.sidebar.markdown('---')

# st.sidebar.markdown("---")

PAGE_DICT = {
    "What is FinComplyAI? 🧠": show_intro,
    "Transaction Analysis Calculations": show_tac,
    "Transaction Analysis Report": show_tar,
    "Financial Visualization": show_viz,
    "Finbot": show_bot
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")


#***********************************************************************************************

if page == "What is FinComplyAI? 🧠": #FIRST PAGE
    show_intro()

#***********************************************************************************************
       
elif page == "Transaction Analysis Calculations": #SECOND PAGE
    show_tac()
    
#***********************************************************************************************

elif page == "Transaction Analysis Report": #THIRD PAGE
    show_tar()

#***********************************************************************************************

elif page == "Financial Visualization": #THIRD PAGE
    show_viz()

#***********************************************************************************************

elif page == "Finbot": #THIRD PAGE
    show_bot()

#***********************************************************************************************
