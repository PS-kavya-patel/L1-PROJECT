import streamlit as st
import os
import pypdf
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq

# Streamlit UI Setup
st.set_page_config(page_title="Ultra-Simple SDS AI", page_icon="🧪")
st.title("SDSense AI – Minimalist RAG")
st.write("A pure Python implementation of RAG using TF-IDF for local search and Groq for fast AI answers!")

# Sidebar for API key and File Upload
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Groq API Key", type="password")
    st.markdown("[Get your free Groq API key here](https://console.groq.com/keys)")
    
    st.header("Document Upload")
    uploaded_file = st.file_uploader("Upload SDS PDF", type=["pdf"])
    process_btn = st.button("Process Document")

# Configure Groq Client if key is provided
client = None
if api_key:
    client = Groq(api_key=api_key)

# Initialize Session State
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "vectorizer" not in st.session_state:
    st.session_state.vectorizer = None
if "tfidf_matrix" not in st.session_state:
    st.session_state.tfidf_matrix = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def extract_text_from_pdf(file):
    """Read text from a PDF file using pypdf."""
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into smaller chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# Handle Document Processing
if process_btn:
    if not api_key:
        st.error("Please enter your Groq API Key first.")
    elif not uploaded_file:
        st.error("Please upload a PDF document.")
    else:
        with st.spinner("Extracting text from PDF..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            
        with st.spinner("Chunking text..."):
            chunks = chunk_text(raw_text)
            
        with st.spinner("Building local search index (TF-IDF)..."):
            try:
                # We limit chunks to keep it fast for this MVP
                chunks = chunks[:50]
                st.session_state.chunks = chunks
                
                # Build TF-IDF matrix locally (No API required!)
                vectorizer = TfidfVectorizer(stop_words='english')
                tfidf_matrix = vectorizer.fit_transform(chunks)
                
                st.session_state.vectorizer = vectorizer
                st.session_state.tfidf_matrix = tfidf_matrix
                
                st.success(f"Processed! Created {len(chunks)} local search chunks.")
            except Exception as e:
                st.error(f"Error processing chunks: {e}")

# Chat Interface
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about the SDS..."):
    if st.session_state.vectorizer is None:
        st.warning("Please upload and process a document first.")
    elif not api_key:
        st.error("Please enter your Groq API Key.")
    else:
        # Save and show user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # 1. Transform the user's query locally
                    query_vec = st.session_state.vectorizer.transform([prompt])
                    
                    # 2. Find the most similar chunks (Cosine Similarity)
                    sims = cosine_similarity(query_vec, st.session_state.tfidf_matrix).flatten()
                    
                    # Sort by similarity and pick the top 3 chunks
                    top_indices = sims.argsort()[-3:][::-1]
                    top_chunks = [st.session_state.chunks[i] for i in top_indices if sims[i] > 0]
                    
                    if not top_chunks:
                        context = "No relevant context found in the document."
                    else:
                        context = "\n\n---\n\n".join(top_chunks)
                    
                    # 3. Ask Groq the question using the context
                    prompt_text = f"""
                    You are a Safety Data Sheet (SDS) Assistant. 
                    Answer the user's question using ONLY the provided context below.
                    If the answer is not in the context, say "I don't know based on the document."
                    
                    CONTEXT:
                    {context}
                    
                    QUESTION: {prompt}
                    """
                    
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": prompt_text,
                            }
                        ],
                        model="llama-3.1-8b-instant",
                    )
                    answer = chat_completion.choices[0].message.content
                    
                    # Show answer
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    
                except Exception as e:
                    st.error(f"Error generating answer: {e}")
