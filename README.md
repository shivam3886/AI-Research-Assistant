# AI-Research-Assistant

## Overview

AI Research Assistant is a simple AI-powered application that allows users to upload PDF documents and ask questions about their content. The system extracts text from uploaded PDFs and uses a Large Language Model (LLM) to generate contextual answers.

## Features

* Upload PDF documents
* Extract text automatically
* Ask questions about the document
* AI-generated answers based on document content
* Simple Streamlit web interface

## Technology Stack

* Python
* Streamlit
* OpenRouter API
* Llama 3.1 8B Instruct
* PyPDF

## Workflow

1. User uploads a PDF.
2. Text is extracted from the document.
3. User enters a question.
4. The document text and question are sent to the LLM.
5. The AI generates an answer based on the document.

## Project Structure

AI-Research-Assistant/
├── app.py
├── README.md
└── requirements.txt

## Future Improvements

* Retrieval-Augmented Generation (RAG)
* Vector Database Integration (ChromaDB/Pinecone)
* Source Citations
* Multi-document Support
* Chat History

## Business Impact

The solution reduces the time required to review large documents and helps users quickly retrieve important information from research papers, reports, and resumes.

## Author

Shivam Verma
