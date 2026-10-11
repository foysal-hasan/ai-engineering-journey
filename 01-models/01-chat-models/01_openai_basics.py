from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the .env file located in the same directory as this script
load_dotenv(override=True)


model = ChatOpenAI(model="gpt-4o-mini")
response = model.invoke("Hello, AI Engineering!")
print(response.content)