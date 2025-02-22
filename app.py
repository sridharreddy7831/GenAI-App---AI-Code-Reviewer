import os
import openai

import streamlit as st

# Load API key securely
OPENAI_API_KEY = os.getenv("ENTER YOUR API KEY")  # Ensure you set this in your environment variables
openai.api_key = OPENAI_API_KEY


def main():
    st.title("GenAI App - AI Code Reviewer")

    code_input = st.text_area("Enter your Python code here:")

    if st.button("Generate"):
        if code_input.strip() == "":
            st.warning("Please enter some Python code.")
        else:
            feedback = analyze_code(code_input)
            st.subheader("Code Review:")
            st.write(feedback)


def analyze_code(code):
    try:
        system_prompt = f"""You are an expert Python code reviewer focusing on identifying bugs, errors, and areas for improvement.
        Analyze the following code and provide a comprehensive report:

        - Clearly describe any bugs or errors found, explaining their potential consequences.
        - Suggest fixes or improvements for each identified issue, including code examples if applicable.
        - If no significant issues are found, provide general feedback on code quality and potential optimizations.

        ## Python Code:      
        {code}
        """

        response = openai.ChatCompletion.create(  # Fix: Use 'openai.ChatCompletion.create'
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_prompt}],
        )

        return response["choices"][0]["message"]["content"]  # Fix: Updated response parsing

    except Exception as e:
        return f"An error occurred: {e}"



if __name__ == "__main__":
    main()
