import streamlit as st
from openai import OpenAI
from pypdf import PdfReader

# Paste your OpenRouter API key here
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY"
)

st.title("AI Research Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    pdf_reader = PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.success("PDF uploaded successfully!")

    question = st.text_input("Ask a question about the PDF")

    if question:
        prompt = f"""
        Based on the document below, answer the user's question.

        DOCUMENT:
        {text}

        QUESTION:
        {question}
        """

        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("Answer")
        st.write(response.choices[0].message.content)
