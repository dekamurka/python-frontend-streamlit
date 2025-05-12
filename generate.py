import streamlit as st
from string import ascii_letters, digits, punctuation
import random


st.title("Generate your password")

spec_char = st.checkbox("Add punctuation")

len = st.slider("Длина",0,24,16)

if st.button("Generate"):
    char = ascii_letters + digits
    if spec_char:
        char += punctuation
    password = "".join(random.choices(char, k=len))
    st.code(password, language="text")