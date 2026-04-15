import streamlit as st
from app.generator import generate_email

st.title("📧 Email Generation Assistant")

intent = st.text_input("Intent")
facts = st.text_area("Key Facts (separate with ;) ")
tone = st.selectbox("Tone", ["formal", "casual", "urgent", "empathetic"])

if st.button("Generate Email"):
    email = generate_email(intent, facts, tone)
    st.subheader("Generated Email:")
    st.write(email)