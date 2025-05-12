import streamlit as st
import requests

def get_rates():
    url = "https://open.er-api.com/v6/latest/RUB"
    inverse_rates = requests.get(url).json()["rates"]
    return {x: 1 / y for x, y in inverse_rates.items()}

st.title("Currency converter")
col1, col2 = st.columns(2)
x = col1.number_input("", min_value=0.0,value=1.0, step=1.0)

r = get_rates()

currency = col2.selectbox("Value", list(r))

st.success(f"{x * r[currency]:,.2f} RUB")

