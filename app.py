import streamlit as st
string = "Subtraction"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Subtraction')
x = st.number_input('Enter a number')
Y = st.number_input('Enter another number')
Z = x-y
st.write("difference is",z)
    