import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load the local .env file residing in this folder
load_dotenv(override=True)

# Verify API key is present
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found in the local .env file.")
    sys.exit(1)

# 2. Initialize the chat model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

print("🤖 LangChain Terminal Assistant Initialized!")
# Get user input from the terminal
user_input = input("\033[92mYou:\033[0m ").strip()

response = model.invoke(user_input)
print(f"\033[96mAI:\033[0m {response.content}")
