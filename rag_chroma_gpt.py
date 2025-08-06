
"""
RAG (Retrieval-Augmented Generation) System with ChromaDB and OpenAI GPT

This module implements a complete RAG pipeline that combines vector similarity search 
with large language model capabilities for intelligent document querying and analysis.

Features:
- Connects to existing ChromaDB vector database
- Performs semantic similarity search using OpenAI embeddings
- Implements Maximum Marginal Relevance (MMR) retrieval for diverse results
- Generates structured responses with sentiment analysis using ChatGPT
- Returns JSON-formatted output with sentiment classification and summaries

Architecture:
1. Vector Retrieval: Uses ChromaDB with OpenAI text-embedding-3-large model
2. Document Search: Implements both similarity search and MMR retrieval methods
3. LLM Processing: Leverages ChatGPT-4o-mini for structured output generation
4. Response Schema: Pydantic models ensure consistent JSON response format

Prerequisites:
- ChromaDB server running on localhost:8000
- OpenAI API key configured in .env file
- Pre-vectorized documents in ChromaDB collection 'digital_leader'
"""
########below code -  openai embedding, connect to chroma db , get embedding for user query with query similary search, pass the returned results to chatgpt model for summary details##############
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import os
import chromadb
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Set up the ChromaDB client 
collection_name = "digital_leader"
chroma_client = chromadb.HttpClient(host='localhost', port=8000)
collection = chroma_client.get_or_create_collection(name=collection_name) 
vectordb = Chroma(
    collection_name=collection_name,  # Unique collection name
    embedding_function=embeddings,
    client= chroma_client
)

# Example: user query to chroma db
query = "What is new societal expectations"


# using similarity search - fetches similar text data
results = vectordb.similarity_search(query, k=3)

print("==================================User Query Results from ChromaDB - SIMILARITY SEARCH==============================================")
# Display results
passage = ""
counter = 0
for result in results:
    print(f"*******************************Result {counter}*************************************")
    print(result)
    passage = passage + result.page_content
    counter += 1


### using retrievers - fetches most relevant data
#https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.as_retriever
retriever = vectordb.as_retriever(
    search_type="mmr", search_kwargs={"k": 3, "fetch_k": 5}
)

results = retriever.invoke(query)

print("==================================User Query Results from ChromaDB - RETRIEVERS==============================================")
# Display results
passage = ""
counter = 0
for result in results:
    print(f"*******************************Result {counter} *************************************")
    print(result)
    passage = passage + result.page_content
    counter += 1



# Define a structured output model for classification
# https://python.langchain.com/docs/tutorials/classification/
class Classification(BaseModel):
    sentiment: str = Field(..., enum=["happy", "neutral", "sad"])
    summary: str = Field(
        ...,
        description="summary information",
    )
    
model = ChatOpenAI(model="gpt-4o-mini",temperature=1).with_structured_output(
    Classification
)


prompt_format = ChatPromptTemplate.from_template(
    """
Extract the desired summary information from the following passage for a given user input.

Only extract the properties mentioned in the 'Classification' function.


Passage:
{passage}

user_input:
{input}
"""
)
# Invoke the prompt with the passage and user input
prompt = prompt_format.invoke({"passage": passage, "input": query})

# Call the model with the prompt to get the structured response
"""
Sample Output:
{
  "sentiment": "neutral",
  "summary": "Millennials and members of Generation Z seek purpose and fulfillment from their work, indicating a shift in societal expectations around employment."
}
"""
response = model.invoke(prompt)
print("==========================Sentiment response from ChatGPT model==============================================")
print(response.model_dump_json(indent=2))
