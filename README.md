> **⚠️ POC DISCLAIMER: This is a Proof of Concept (POC) implementation. Please do not evaluate this code for production-level code structure, modularity, or best practices. This project is designed for educational and demonstration purposes only.**

# AI-RAG: Retrieval-Augmented Generation System

A sophisticated **Retrieval-Augmented Generation (RAG) system** that combines **document vectorization**, **semantic search**, and **large language model capabilities** for intelligent document querying and analysis. This system enables natural language queries against PDF documents while providing structured responses with sentiment analysis.

## 📋 Table of Contents

- [Complete Processing Flow](#-complete-processing-flow)
- [Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setup ChromaDB](#setup-chromadb)
  - [Set up OpenAI Key](#set-up-openai-key)
  - [Run code to test Retrieval Augmented Generation](#run-code-to-test-retrieval-augmented-generation)
- [Project Structure](#-project-structure)
- [Modules](#-modules)
  - [document_vectorization.py](#-document_vectorizationpy)
  - [rag_chroma_gpt.py](#-rag_chroma_gptpy)
  - [Workflow Integration](#-workflow-integration)
- [Sample Output](#sample-output)


## 🔄 Complete Processing Flow

When a user queries the system with *"What is new societal expectations"*:

1. **📄 Document Ingestion**: PDF documents are loaded and processed using PyPDFLoader
2. **✂️ Text Chunking**: Documents split into 1000-character chunks with 300-char overlap for context preservation
3. **🔗 Vectorization**: Text chunks converted to embeddings using OpenAI text-embedding-3-large model
4. **💾 Vector Storage**: Embeddings stored in ChromaDB with unique identifiers for efficient retrieval
5. **🔍 Similarity Search**: User query vectorized and matched against stored document embeddings
6. **📊 Retrieval Methods**: Both similarity search and MMR (Maximum Marginal Relevance) retrieval implemented
7. **🤖 LLM Processing**: Retrieved context passed to ChatGPT-4o-mini for structured analysis
8. **📝 Structured Output**: Response formatted with sentiment analysis and summary using Pydantic models
9. **📨 JSON Response**: Final output delivered as structured JSON with sentiment classification
10. **✅ Complete Analysis**: User receives comprehensive answer with source context and metadata

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Docker (for ChromaDB)
- OpenAI API key
- PDF document for processing
- Required dependencies (see `requirements.txt`)

### Installation 

```bash
# Clone or navigate to the project directory
cd $HOME$/ai-rag

# install with pip
python3 -m venv ai-rag
source ai-rag/bin/activate

# Install dependencies
pip install -r requirements.txt

```

### Setup ChromaDB

```bash
# Pull and run ChromaDB container
docker pull chromadb/chroma
docker run -p 8000:8000 chromadb/chroma
```

### Set up OpenAI Key
In .env file at the root of project configure your OPEN_API_KEY
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Run code to test Retrieval Gugmented Generation

```bash
# Step 1: Vectorize your PDF document
python3 document_vectorization.py

# Step 2: Query the vectorized documents
python3 rag_chroma_gpt.py
```

## 📁 Project Structure

```
ai-rag/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (create this)
├── digital-leader.pdf          # Sample PDF document
├── document_vectorization.py   # Document processing and vectorization
└── rag_chroma_gpt.py           # RAG query system with LLM integration
```

## 🔧 Modules

### 📄 `document_vectorization.py`
**Purpose**: Document ingestion and vectorization pipeline
- **Features**:
  - PDF document loading and text extraction
  - Intelligent text chunking with overlap preservation
  - OpenAI embedding generation for semantic similarity
  - ChromaDB vector storage with unique document IDs
  - Basic similarity search validation
- **Configuration**:
  - Chunk Size: 1000 characters
  - Chunk Overlap: 300 characters  
  - Embedding Model: text-embedding-3-large
  - Collection: 'digital_leader'
- **Output**: Vectorized document chunks stored in ChromaDB

### 🤖 `rag_chroma_gpt.py`
**Purpose**: RAG query system with LLM-powered analysis
- **Features**:
  - Connects to existing ChromaDB vector database
  - Performs semantic similarity search using OpenAI embeddings
  - Implements Maximum Marginal Relevance (MMR) retrieval
  - Generates structured responses with sentiment analysis
  - Returns JSON-formatted output with Pydantic validation
- **Architecture**:
  - Vector Retrieval: ChromaDB with OpenAI embeddings
  - Document Search: Similarity search and MMR retrieval
  - LLM Processing: ChatGPT-4o-mini for structured output
  - Response Schema: Pydantic models for consistent formatting
- **Output**: Structured JSON with sentiment classification and summaries

### 🔄 Workflow Integration
1. Run `document_vectorization.py` first to prepare your document corpus
2. Use `rag_chroma_gpt.py` for intelligent querying and analysis
3. Both modules work together to provide end-to-end RAG capabilities

## Sample Output

```bash
(ai-rag) satish@Satishs-Air ai-rag % python3 document_vectorization.py
==================================User Query Results from ChromaDB==============================================
*******************************Page 0*************************************
than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from
*******************************Page 1*************************************
than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from
*******************************Page 2*************************************
than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from
```





```bash
(ai-rag) satish@Satishs-Air ai-rag % python3 rag_chroma_gpt.py
==================================User Query Results from ChromaDB - SIMILARITY SEARCH==============================================
*******************************Result 0*************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
*******************************Result 1*************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
*******************************Result 2*************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
==================================User Query Results from ChromaDB - RETRIEVERS==============================================
*******************************Result 0 *************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
*******************************Result 1 *************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
*******************************Result 2 *************************************
page_content='than ever.
New employee expectations.
Information has become democratized 
both inside and outside of companies. 
In the past, CEOs and other senior 
leaders were seen as the legitimate 
strategic decision-makers because 
they had more access to data and 
could decide if and when to share it. 
With much more information available 
to many more people, leaders’ 
legitimacy must come from different 
sources, or they must share decision-
making with employees—or both.
Workers increasingly resist one-way, 
top-down communication and 
commands; they expect to be heard 
and to help develop their organizations’ 
plans and solutions collaboratively. 
They take the responsibility that comes 
with “co-creation” seriously, with 
younger generations of employees 
ready to be judged on their creativity 
as much as their expertise.
New societal expectations.
Roundtable participants said that 
Millennials and members of Generation 
Z seek purpose and fulfillment from' metadata={'source': 'tweet'}
==========================Sentiment response from ChatGPT model==============================================
{
  "sentiment": "neutral",
  "summary": "Millennials and members of Generation Z seek purpose and fulfillment with new societal expectations."
}
```
