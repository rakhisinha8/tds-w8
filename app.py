import streamlit as st
string = "Subtraction"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Subtraction')
x = st.number_input('Enter a number')
y = st.number_input('Enter another number')
z = x-y
st.write("difference is",z)
    
