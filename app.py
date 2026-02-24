import streamlit as st #enable Streamlit

st.write("Hooray, we connected everything")

with open("README.md") as f:
    readme_bytes = f.read()

st.download_button(label="Little Git Cheatsheet ;)", data=readme_bytes, file_name="README.md", mime="text/markdown")