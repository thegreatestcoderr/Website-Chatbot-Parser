import clsgoogle.generativeai as genai
import os

# Option 1: Set the API key as an environment variable
#api_key = os.environ.get("GOOGLE_API_KEY")
api_key = "AIzaSyBNA4ikJu7rh_e5lDATzdt4MGg3sRG0Rxo"
if not api_key:
    print("Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

# Option 2: Directly pass your API key (less secure for sharing)
# genai.configure(api_key="YOUR_API_KEY")