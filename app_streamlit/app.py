import streamlit as st
import requests

st.title("DeutschAI Tutor 🇩🇪🤖")

BACKEND_URL = st.secrets.get("BACKEND_URL", "http://localhost:8000")

text = st.text_area("Wpisz zdanie po niemiecku")

if st.button("Sprawdź"):
    res = requests.post(f"{BACKEND_URL}/correct", json={"text": text}).json()
    st.subheader("Poprawione:")
    st.write(res.get("corrected", "—"))
    st.subheader("Wyjaśnienie:")
    st.write(res.get("explanation", "—"))
