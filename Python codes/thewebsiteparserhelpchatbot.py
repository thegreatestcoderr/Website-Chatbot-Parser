import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ---------- 1. Crawl website ----------

def crawl_website(start_url, max_pages=50):
    visited = set()
    queue = deque([start_url])
    domain = urlparse(start_url).netloc
    pages = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            print(f"Crawling: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed: {url} ({e})")
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n", strip=True)
        if not text:
            continue

        pages.append({"url": url, "text": text})

        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)

            if parsed.netloc == domain and full_url not in visited:
                queue.append(full_url)

    return pages


# ---------- 2. Chunk + embed + store in vector DB ----------

def build_vector_store(pages, persist_dir="chroma_db"):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )

    texts = []
    metadatas = []

    for page in pages:
        chunks = splitter.split_text(page["text"])
        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({"url": page["url"]})

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    db = Chroma(
        collection_name="website_rag",
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )

    print(f"Adding {len(texts)} chunks to vector store...")
    db.add_texts(texts=texts, metadatas=metadatas)
    db.persist()

    return db


# ---------- 3. Build RAG chain ----------

def build_rag_chain(vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    system_template = """
You are an expert assistant that answers questions using ONLY the provided context.

Context:
{context}

Rules:
- If the answer is not in the context, say:
  "I can only answer questions based on the website information I have."
- Do NOT invent or guess.
- Cite relevant parts of the context when helpful.
"""

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_template),
            ("human", "Question: {question}\nAnswer:"),
        ]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.2,
    )

    def rag_chain(question: str) -> str:
        docs = retriever.get_relevant_documents(question)
        context = "\n\n---\n\n".join(d.page_content for d in docs)
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"context": context, "question": question})

    return rag_chain


# ---------- 4. Chat loop ----------

def chat_loop(rag_fn):
    print("RAG Website Assistant ready! (type 'exit' to quit)")
    while True:
        q = input("You: ")
        if q.lower().strip() == "exit":
            print("Assistant: Goodbye!")
            break
        answer = rag_fn(q)
        print(f"\nAssistant: {answer}\n")


# ---------- 5. Main ----------

if __name__ == "__main__":
    load_dotenv()

    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY not set. Add it to your .env file.")
        exit(1)

    print("Enter the website URL you want to crawl:")
    target_url = input("> ").strip()

    print("\nStarting crawl...\n")
    pages = crawl_website(target_url, max_pages=50)

    if not pages:
        print("No pages scraped. Exiting.")
        exit(1)

    print("\nBuilding vector store...\n")
    db = build_vector_store(pages)

    print("\nBuilding RAG chain...\n")
    rag = build_rag_chain(db)

    chat_loop(rag)
