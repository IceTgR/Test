import streamlit as st #enable Streamlit

st.write("Hooray, we connected everything")
st.download_button("Little Git Cheatsheet ;)", data=readme, file_name="README.md")