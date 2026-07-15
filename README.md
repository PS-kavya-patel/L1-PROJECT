# Simple SDS AI (Minimalist RAG)

A lightweight, purely local Retrieval-Augmented Generation (RAG) application built with Python and Streamlit. This app allows you to upload Safety Data Sheet (SDS) PDFs, automatically processes them using TF-IDF for local search, and answers your questions using the Groq API.

![App Screenshot 1](./screenshot1.png)
![App Screenshot 2](./screenshot2.png)

## Features
- **No External Vector Database:** Uses `scikit-learn`'s `TfidfVectorizer` and `cosine_similarity` for completely local, in-memory text search.
- **Fast Generation:** Uses Groq's API (`llama-3.1-8b-instant`) to instantly generate answers based strictly on your document.
- **Minimalist:** Everything runs from a single `app.py` script.

## How It Works
1. **Upload:** Upload an SDS PDF file.
2. **Chunk & Index:** The text is extracted, chunked (1000 characters), and indexed into vectors locally using TF-IDF.
3. **Search:** Your question is compared against the chunks using Cosine Similarity to find the 3 most relevant sections.
4. **Answer:** The top 3 chunks are sent to the Groq LLM to generate an accurate answer based solely on the document.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`

## Requirements
To run this project, you will need a [Groq API Key](https://console.groq.com/keys).
