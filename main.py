import streamlit as st

st.set_page_config(page_title="Free File Converter", page_icon=":tada:", layout="wide")

# header
st.subheader("This is a free converter for ALL file types!")


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
