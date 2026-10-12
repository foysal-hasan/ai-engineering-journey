from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)
result = chain.invoke({ 'topic': 'AI'})
print(result)
