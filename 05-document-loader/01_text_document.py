from pathlib import Path
from langchain_community.document_loaders import TextLoader

current_dir = Path(__file__).resolve().parent
loader = TextLoader(current_dir / 'cricket.txt', encoding='utf-8')

docs = loader.load()
print(docs)
print(type(docs))