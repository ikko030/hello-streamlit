import streamlit as st

x=st.slider('Select a value')
st.write(x,'is a square',x*x)

st.title('this is the app tiltle ')
st.header('this is the markdown')
st.markdown('this is the header')
st.subheader('this is the subheader')
st.caption('this is the caption')
st.code('x=2024')
st.latex(r'''a+ar^1+ar^2+ar^3''')
