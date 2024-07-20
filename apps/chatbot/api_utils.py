# import os
# import base64

# def get_encoded_api_key():
#     """
#     Retrieves the OpenAI API key from the environment variable and encodes it using Base64.
    
#     Returns:
#         str: The Base64-encoded OpenAI API key.
#     """
#     api_key = os.getenv("OPENAI_API_KEY")
#     encoded_api_key = base64.b64encode(api_key.encode()).decode()
#     return encoded_api_key


# utils.py
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-7dY4TkqmIV7TV3joNuGVT3BlbkFJVSU9C0LduVUwQYUTtXbz'

def generate_exercise(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate model name
        prompt=prompt,
        max_tokens=150  # Adjust tokens as needed
    )
    return response.choices[0].text.strip()

def generate_hint(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

