from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

joke_prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

explaination_prompt = PromptTemplate(
    template='Explain the joke: {joke}',
    input_variables=['joke']
)


model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

joke_chain = RunnableSequence(joke_prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explaination": RunnableSequence(explaination_prompt, model, parser)
})

chain = RunnableSequence(joke_chain, parallel_chain)
result = chain.invoke({ 'topic': 'AI'})
print(result)
