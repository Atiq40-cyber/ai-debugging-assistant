import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from utils.llm_client import GeminiClient
from utils.debugging_helper import build_debugging_prompt


def main():
    st.set_page_config(
        page_title= "AI Debugging Assistant",
        page_icon="🔎",
        layout="centered"
    )

    st.title("🔧 AI Debugging Assistant")
    st.write("Paste your **Python Code** or **error log**, and I'll help you debug it.")

    user_input = st.text_area(
        "Enter your code or error log below:",
        height=200,
        placeholder="Example:\nprint(Hello World)"
    )

    if st.button("🔎 Debug Code"):
        if not user_input.strip():
            st.warning("Please enter some code or error message.")
            return
        with st.spinner("Analyzing your code.."):
            try:
                prompt = build_debugging_prompt(user_input)
                client = GeminiClient()
                response = client.ask(prompt)

                st.markdown("---")
                st.subheader("🧠 Debugging Result")
                st.markdown(response)
                

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__=="__main__":
    main()