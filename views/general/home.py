import streamlit as st

st.markdown("# Welcome!")

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
            
_Roll The Dice_ is a statistics calculator with the goal of making things simpler than using code or a graphing calculator. It is made by me, **Corey Michaud** :)
            
This, in theory, will forever be a **work in progress**, so this should be updated whenever I have time to do so, or need to use a formula that isn't yet implemented.

""")
    
with col2:
    st.image("images/corey.jpg", caption = "Me")

st.markdown("""
            
# A Little About Me
            
Is this back to normal? SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT 
SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT SAMPLE TEXT 

# How It's Made

This site is made using Streamlit with Python, and is hosted on Streamlit Cloud. The code is open source and can be found on [GitHub](https://github.com/coreymichaud).
    
""")