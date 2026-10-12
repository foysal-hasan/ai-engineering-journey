from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

current_dir = Path(__file__).resolve().parent
loader = PyPDFLoader(current_dir / 'sample.pdf')

docs = loader.load()

print(len(docs))
print(type(docs))