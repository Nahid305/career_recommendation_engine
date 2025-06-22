import streamlit as st
import cohere

# Securely load API key from Streamlit secrets
co = cohere.Client(st.secrets["cohere"]["api_key"])

def ask_career_bot(prompt):
    try:
        response = co.chat(
            model="command-r",
            message=prompt,
            temperature=0.7
        )
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"
