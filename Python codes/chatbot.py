import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


if "GOOGLE_API_KEY" not in os.environ:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set your Gemini API key in your system environment or in a .env file.")
    exit(1)


chess_info_text = ""
try:
    with open('website_text.txt', 'r', encoding='utf-8') as f:
        chess_info_text = f.read()
except UnicodeDecodeError:
    print("UTF-8 decoding failed for 'website_text.txt'. Trying 'windows-1252'...")
    try:
        with open('website_text.txt', 'r', encoding='windows-1252') as f:
            chess_info_text = f.read()
    except Exception as e:
        print(f"Error reading 'website_text.txt' with windows-1252 encoding: {e}")
        print("Please ensure 'website_text.txt' is correctly encoded or re-save it as UTF-8.")
        exit(1)
except FileNotFoundError:
    print("Error: 'website_text.txt' not found.")
    print("Please run your web scraping script first to create 'website_text.txt'.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred while opening 'website_text.txt': {e}")
    exit(1)


chess_expert_template = f"""
You are a highly knowledgeable chess expert. Your goal is to answer questions about chess
based *only* on the information provided in the following context.

Context:
{chess_info_text}

If the user asks a question that cannot be answered from the provided context,
or is not related to chess, respond with 'I can only answer questions about chess based on the information I have.'

Question: {{question}}
Answer:
"""

chess_expert_prompt_template = ChatPromptTemplate.from_template(chess_expert_template)
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.2) 


llm_chain = chess_expert_prompt_template | llm | StrOutputParser()

def query_llm(question):
    response_text = llm_chain.invoke({'question': question})
    print(f"Chess Expert: {response_text}")


print("Hello! I am a chess GrandMaster! Ask me any questions related to chess! (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chess Expert: Goodbye! Keep practicing your chess!")
        break
    query_llm(user_input)