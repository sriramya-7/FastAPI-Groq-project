import streamlit as st
import requests
import os


API = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
print(API)

st.title("Prompt → Groq (FastAPI + Streamlit)")
prompt = st.text_area("Enter your prompt:", height=120)


if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Calling API..."):
            try:
                r = requests.post(f"{API}/api/generate", json={"prompt": prompt}, timeout=60)
                if r.ok:
                    st.subheader("Response")
                    st.write(r.json().get("response", ""))
                else:
                    st.error(f"API error ({r.status_code}): {r.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")