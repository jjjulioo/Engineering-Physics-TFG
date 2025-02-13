from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

print(api_key)  # Should print your key


client = OpenAI(api_key)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  store=True,
  messages=[
    {"role": "user", "content": "Hi, how are you?"}
  ]
)

print(completion.choices[0].message)