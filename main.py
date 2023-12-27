import streamlit as st
import pandas as pd
from io import StringIO

with st.sidebar:
    selected = option_menu(
        "Choose conversion",
        ["JSON to TOML", "Converter #02 (TBC)", "Converter #03 (TBC)"],
        icons=["gear"],
        # menu_icon="bookmark-fill",
        menu_icon="robot",
        default_index=0,
    )
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

st.set_page_config(page_title="Free File Converter", page_icon=":tada:", layout="wide")

# header
st.subheader("This is a free converter for ALL file types!")


#if st.button('Say hello'):
#    st.write('Why hello there')
#else:
#    st.write('Goodbye')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
