# AI Terminology - Learning Notes

This document contains the fundamental AI concepts I learned while studying Generative AI, Large Language Models (LLMs), and modern AI systems.

---

# 1. Artificial Intelligence (AI)

Artificial Intelligence (AI) is the ability of computers to perform tasks that normally require human intelligence.

These tasks include:
- Learning from data
- Understanding language
- Recognizing images
- Making decisions
- Solving problems

Examples:
- ChatGPT
- Siri
- Google Maps
- Netflix Recommendations

---

# 2. Generative AI

Generative AI is a branch of AI that creates new content instead of only analyzing existing information.

It can generate:
- Text
- Images
- Audio
- Videos
- Code

Example:
A prompt like "Write a poem about nature" produces completely new content.

---

# 3. Large Language Model (LLM)

A Large Language Model (LLM) is an AI model trained on massive amounts of text data.

Its primary purpose is to understand and generate human language.

Popular LLMs include:
- GPT
- Gemini
- Claude
- Llama
- Mistral

LLMs are capable of:
- Answering questions
- Writing code
- Summarizing documents
- Translating languages
- Generating content

---

# 4. Multimodal Models

Traditional LLMs mainly process text.

Multimodal models can understand multiple data types including:
- Text
- Images
- Audio
- Video
- Documents

Example:
Uploading an image and asking the AI to describe it.

---

# 5. Llama

Llama is an open-source family of Large Language Models developed by Meta.

It is widely used for:
- Research
- AI applications
- Fine-tuning custom models

---

# 6. Neural Network

A Neural Network is the core technology behind modern AI.

It is inspired by the structure of the human brain.

A neural network learns patterns from data instead of following fixed rules.

Example:
After training on thousands of cat images, it learns how to recognize cats in new images.

---

# 7. Neural Network Architecture

Architecture refers to how a neural network is designed.

It defines:
- Number of layers
- Connections between neurons
- Information flow

Examples:
- CNN (Computer Vision)
- RNN (Sequential Data)
- Transformer (Large Language Models)

Modern LLMs use the Transformer architecture.

---

# 8. RLHF (Reinforcement Learning from Human Feedback)

RLHF improves AI responses using human feedback.

Process:
1. AI generates multiple responses.
2. Humans rank the responses.
3. AI learns which responses are preferred.
4. Future responses become more accurate and helpful.

Purpose:
Improve quality, safety, and alignment with human expectations.

---

# 9. Data Labeling

Data labeling is the process of assigning correct labels to training data.

Example:

Image → Label

🐱 → Cat

🚗 → Car

🌳 → Tree

The labeled data helps AI learn patterns correctly.

---

# 10. Instruction Tuning

Instruction Tuning teaches an AI model how to follow user instructions.

Instead of predicting only the next word, it learns how to perform tasks such as:
- Summarization
- Translation
- Question answering
- Code generation

This makes AI assistants much more useful.

---

# 11. Context Window

The Context Window is the amount of information an AI model can remember during a conversation.

A larger context window allows the model to:
- Read long documents
- Maintain longer conversations
- Remember previous messages

Example:
A 128K context window can process hundreds of pages of text in one interaction.

---

# Modern AI Concepts

## 1. Agentic AI

Agentic AI refers to AI systems that can plan, reason, and execute tasks autonomously.

Capabilities include:
- Planning
- Decision making
- Tool usage
- Multi-step workflows

Example:
Booking a flight after comparing prices across websites.

---

## 2. Large Reasoning Model (LRM)

A Large Reasoning Model focuses on solving complex problems through logical reasoning.

Common applications:
- Mathematics
- Programming
- Scientific reasoning
- Complex decision-making

Unlike traditional LLMs, LRMs emphasize reasoning quality over speed.

---

## 3. Vector Database

A Vector Database stores information as embeddings (vectors) instead of plain text.

Benefits:
- Semantic search
- Similarity search
- Fast retrieval

Popular databases:
- FAISS
- Pinecone
- Chroma
- Milvus

---

## 4. Retrieval-Augmented Generation (RAG)

RAG combines document retrieval with an LLM.

Workflow:

User Question
↓
Convert Question to Vector
↓
Search Vector Database
↓
Retrieve Relevant Documents
↓
Provide Context to LLM
↓
Generate Accurate Answer

Advantages:
- Uses private documents
- Reduces hallucinations
- Produces more accurate answers

---

## 5. Model Context Protocol (MCP)

Model Context Protocol (MCP) is a standard protocol that allows AI models to securely connect with external tools and data sources.

Examples:
- File systems
- Databases
- APIs
- GitHub
- Google Drive

MCP provides a common interface between AI models and external systems.

---

## 6. Mixture of Experts (MoE)

Mixture of Experts is an AI architecture where multiple specialized models (experts) exist inside one large model.

Instead of activating the entire model, only the most relevant experts are used for a specific task.

Benefits:
- Faster inference
- Lower computational cost
- Improved performance

---

## 7. Artificial Super Intelligence (ASI)

Artificial Super Intelligence (ASI) is a hypothetical future AI that would outperform humans across nearly every intellectual task.

Potential capabilities include:
- Scientific research
- Engineering
- Medicine
- Creativity
- Strategic planning

ASI does not currently exist.

---

# AI Learning Pipeline

Raw Data
↓
Data Collection
↓
Data Labeling
↓
Neural Network Training
↓
Large Language Model (LLM)
↓
Instruction Tuning
↓
RLHF
↓
Multimodal AI
↓
AI Agents
↓
Vector Database
↓
RAG
↓
Advanced Architectures (MoE / LRM)
↓
Future AI (ASI)

---

# Summary

| Concept | Description |
|----------|-------------|
| AI | Machines performing intelligent tasks |
| Generative AI | AI that creates new content |
| LLM | AI trained on large-scale text data |
| Multimodal | AI understands multiple data types |
| Llama | Open-source LLM family by Meta |
| Neural Network | Learning system inspired by the brain |
| Architecture | Structure of a neural network |
| RLHF | Learning from human feedback |
| Data Labeling | Adding labels to training data |
| Instruction Tuning | Teaching models to follow instructions |
| Context Window | Information the model can remember |
| Agentic AI | AI capable of autonomous task execution |
| Large Reasoning Model | AI specialized in logical reasoning |
| Vector Database | Stores embeddings for semantic search |
| RAG | Retrieval + Generation using external knowledge |
| MCP | Standard protocol for AI-tool integration |
| MoE | Activates only relevant experts in a model |
| ASI | Hypothetical AI beyond human intelligence |
