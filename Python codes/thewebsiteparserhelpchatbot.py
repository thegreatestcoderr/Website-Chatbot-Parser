import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



def crawl_website(start_url, max_pages=50):
    visited = set()
    queue = deque([start_url])
    domain = urlparse(start_url).netloc
    all_text = []

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

        
        page_text = soup.get_text(separator="\n", strip=True)
        all_text.append(f"\n\n=== PAGE: {url} ===\n\n{page_text}\n")

        
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)

            if parsed.netloc == domain and full_url not in visited:
                queue.append(full_url)

    return "\n".join(all_text)


def save_website_text(text, filename="website_text.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nSaved website text to {filename}\n")




def load_website_text():
    try:
        with open('website_text.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading website_text.txt: {e}")
        exit(1)


def build_chatbot(website_text):
    template = f"""
You are an expert assistant whose job is to answer questions *only* using the information
found in the following website content.

Website Content:
{website_text}

Rules:
- If the answer is not found in the website content, say:
  "I can only answer questions based on the website information I have."
- Do NOT invent or guess.
- Stay strictly within the provided content.

Question: {{question}}
Answer:
"""

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-pro',
        temperature=0.2
    )

    return prompt | llm | StrOutputParser()


def chat_loop(llm_chain):
    print("Website Assistant is ready! Ask anything about the website. (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Website Assistant: Goodbye!")
            break

        answer = llm_chain.invoke({"question": user_input})
        print(f"Website Assistant: {answer}\n")



if __name__ == "__main__":
    load_dotenv()

    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY not set. Add it to your .env file.")
        exit(1)

    print("Enter the website URL you want to crawl:")
    target_url = input("> ").strip()

    print("\nStarting crawl...\n")
    website_text = crawl_website(target_url, max_pages=50)

    save_website_text(website_text)

    print("Loading website into chatbot...\n")
    text = load_website_text()
    chatbot = build_chatbot(text)

    chat_loop(chatbot)
