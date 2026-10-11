import os
import sys
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv


# 1. Load the local .env file residing in this folder
load_dotenv(override=True)

# Verify API key is present
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found in the local .env file.")
    sys.exit(1)

class Review(TypedDict):
    summary: str
    sentiment: str

model = ChatOpenAI()
structured_model = model.with_structured_output(Review)

result = structured_model. invoke("""The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
compared to other brands. Hoping for a software update to fix this. """)

print(result)
print(result['summary' ])
print(result['sentiment' ])