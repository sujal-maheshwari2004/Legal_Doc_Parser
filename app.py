import streamlit as st
from main import main

# Streamlit UI
st.title("Document Information Extractor")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    input_file = uploaded_file.name
    with open(input_file, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Processing... Please wait.")
    main(input_file)
    st.success("Data extraction complete! Check the CSV file.")
