from openai import OpenAI
import os

# Set your API key
#openai.api_key = "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"

client = OpenAI(
  api_key="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"
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  store=True,
  messages=[
    {"role": "user", "content": "Hi, how are you?"}
  ]
)

print(completion.choices[0].message)