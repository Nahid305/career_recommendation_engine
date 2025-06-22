import streamlit as st
import requests
from streamlit_lottie import st_lottie

@st.cache_data(show_spinner=False)
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"  # ✅ Verified working

lottie_data = load_lottie_url(lottie_url)

st.title("🔁 Lottie Animation Test")
if lottie_data:
    st_lottie(lottie_data, height=300)
else:
    st.warning("⚠️ Still can't load animation.")
