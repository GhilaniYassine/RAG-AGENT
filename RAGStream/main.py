#connect to llm
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    azure_endpoint=os.getenv("OPENAI_BASE_URL"),
    api_version="2024-08-01-preview"
)

response = client.chat.completions.create(   
  model="gpt-4o",#  Replace with your actual deployment name from Azure Portal
  messages=[
    {"role": "user", "content": "This is a test."}
  ]
)

print(response.model_dump_json(indent=2))



j
