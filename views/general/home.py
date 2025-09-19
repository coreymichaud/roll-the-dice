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
            
# Motivation

There are a lot of formulas when it comes to statistics, and it's hard to try to memorize them all. In college, statistics is *clearly* the best math subject, so it was the only one that lets you use a calculator or code to solve problems.
Graphing calculators have a lot of functionality, but they don't have everything. That's usually where code comes in, but then you have to remember how to do each test. What if you know how to do a 2-sample Z-interval in R, but
your situation only allows for Python? That's *hopefully* where this site comes in.
            
This site is meant to not only be a calculator for statistics, but a way to learn how to use these formulas. Hopefully, you are able to learn something from using each page.
            
Also, this is for my own personal learning. It would make sense that if I graduated college years ago and never use these formulas, that I would forget them if they ever came up again. This is my way of making sure I don't forget.

# How It's Made

This site is made using Streamlit with Python, and is hosted on Streamlit Cloud. The code is open source and can be found on [GitHub](https://github.com/coreymichaud).
    
""")