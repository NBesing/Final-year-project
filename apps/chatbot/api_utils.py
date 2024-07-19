import os
import base64

def get_encoded_api_key():
    """
    Retrieves the OpenAI API key from the environment variable and encodes it using Base64.
    
    Returns:
        str: The Base64-encoded OpenAI API key.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    encoded_api_key = base64.b64encode(api_key.encode()).decode()
    return encoded_api_key