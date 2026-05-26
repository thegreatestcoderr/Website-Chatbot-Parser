import os
import re
import json
import pdfplumber
from openai import OpenAI

client = OpenAI()

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def normalize_profile(text):
    return {"raw_text": text}

EXTRACTION_PROMPT = """
You are a recruiter assistant. Analyze the following LinkedIn profile text.

Return a JSON object with:
- python_dev: true/false
- python_strength: "strong" | "medium" | "weak"
- evidence: list of quotes from the profile
- frameworks: list of Python-related tools/frameworks mentioned
- seniority: junior/mid/senior
- score: 0–100

Profile text:
{profile}
"""

def extract_profile_info(profile_text):
    prompt = EXTRACTION_PROMPT.format(profile=profile_text)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

def score_candidate(data):
    score = 0
    if data.get("python_dev"):
        score += 40
    strength = data.get("python_strength")
    if strength == "strong":
        score += 30
    elif strength == "medium":
        score += 15
    frameworks = data.get("frameworks", [])
    score += len(frameworks) * 10
    seniority = data.get("seniority")
    if seniority == "senior":
        score += 20
    elif seniority == "mid":
        score += 10
    return score

def process_folder(folder_path):
    results = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            full_path = os.path.join(folder_path, file)
            raw = extract_text_from_pdf(full_path)
            