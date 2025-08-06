
"""
Document Vectorization Pipeline for RAG System

This module implements the document ingestion and vectorization phase of a RAG pipeline.
It processes PDF documents, splits them into semantic chunks, generates embeddings,
and stores them in ChromaDB for efficient similarity search.

Features:
- PDF document loading and text extraction
- Intelligent text chunking with overlap for context preservation
- OpenAI embedding generation for semantic similarity
- ChromaDB vector storage with unique document IDs
- Basic similarity search validation

Prerequisites:
- ChromaDB server running on localhost:8000
- OpenAI API key configured in .env file
- PDF file './digital-leader.pdf' in the working directory

Note: This is the data preparation step. Use rag_chroma_gpt.py for querying
the vectorized documents with LLM-powered analysis.
"""
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import chromadb
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

# change path to your PDF file
pdf_url = "./digital-leader.pdf"
# Load PDF document
pdf_loader = PyPDFLoader(pdf_url)
documents = pdf_loader.load()
# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
texts = text_splitter.split_documents(documents)
# exract text content from the split documents
texts_str = [text.page_content for text in texts]

# Add each text to a Document object with metadata
docs = []
count = 0
for text in texts_str:
    count = count+1
    doc = Document(
    page_content=text,
    metadata={"source": "tweet"},
    id=count,)
    docs.append(doc)

uuids = [str(uuid4()) for _ in range(len(docs))]

# connect to ChromaDB and create a collection and add documents
collection_name = "digital_leader"
chroma_client = chromadb.HttpClient(host='localhost', port=8000)
collection = chroma_client.get_or_create_collection(name=collection_name) 
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectordb = Chroma(
    collection_name=collection_name,  # Unique collection name
    embedding_function=embeddings,
    client=chroma_client
)
vectordb.add_documents(documents=docs, ids=uuids)

# Example: Query the chromadb database
query = "What is new societal expectations"
results = vectordb.similarity_search(query, k=3)

#results = await vector_store.asimilarity_search("When was Nike incorporated?")
# Display results
print("==================================User Query Results from ChromaDB==============================================")
counter = 0
for result in results:
    print(f"*******************************Page {counter}*************************************")
    print(result.page_content)
    counter += 1
