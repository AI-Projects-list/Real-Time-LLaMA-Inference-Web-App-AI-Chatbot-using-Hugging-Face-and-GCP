import streamlit as st
from model_loader import load_model, generate_response

st.title("🦙 LLaMA-powered Chatbot")
prompt = st.text_input("Enter your prompt:")

if prompt:
    model, tokenizer = load_model()
    with st.spinner("Generating..."):
        output = generate_response(prompt, model, tokenizer)
    st.success("Response:")
    st.write(output)