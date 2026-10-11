from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_template = ChatPromptTemplate([
    ('system', "Your are a helpfull customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}")
])

current_dir = Path(__file__).resolve().parent

# load chat history
chat_history = []
with open(current_dir / 'chat_history.txt') as f:
    chat_history.extend(f.readlines())


# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund"
})

print(prompt)
