import streamlit as st #enable Streamlit

st.write("Hello World")

with open("README.md") as f:
    readme_bytes = f.read()


st.download_button(label="Little Git Cheatsheet ;)", data=readme_bytes, file_name="Cheatsheet.md", mime="text/markdown")
