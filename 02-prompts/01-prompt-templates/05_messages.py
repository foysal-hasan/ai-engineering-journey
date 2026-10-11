import os
import sys
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

# Verify API key is present
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found in the local .env file.")
    sys.exit(1)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage("Tell me about langchain")
]

model = ChatOpenAI()

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)