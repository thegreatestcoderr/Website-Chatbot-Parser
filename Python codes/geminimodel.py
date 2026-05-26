import os
import google.generativeai as genai

# Configure the API client with your API key from the environment variable
# This assumes you've set GEMINI_API_KEY='YOUR_API_KEY_HERE' in your system or .env file
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set your API key as an environment variable or pass it directly.")
    exit(1)

# Choose a model (e.g., gemini-pro, gemini-1.5-flash)
model = genai.GenerativeModel('gemini-1.5-flash') # Or 'gemini-pro' for text-only

# Send a prompt to the model
response = model.generate_content("Tell me a short story about a robot who loves to paint.")

# Print the model's response
print(response.text)