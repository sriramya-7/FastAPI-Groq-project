import os
from dotenv import load_dotenv
##*from openai import OpenAI
from groq import Groq

# Load variables from .env into environment (e.g., OPENAI_API_KEY)
load_dotenv()


# Create a single client; it auto-reads OPENAI_API_KEY from the environment
##*client = OpenAI()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

def generate_text(prompt: str) -> str:
    """
    Very basic wrapper around OpenAI's Responses API.
    """
    '''resp = client.responses.create(
        model="gpt-4o-mini",
        model="llama-3.1-8b-instant"
        input=prompt,
    )
    # .output_text is a convenience that concatenates all text outputs
    return resp.output_text'''


    resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",   # replace with any model you have access to
    messages=[
        {"role": "system", "content": "Answer concisely."},
        {"role": "user", "content": prompt},
    ],
    )
    return resp.choices[0].message.content
