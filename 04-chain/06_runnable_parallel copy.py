from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

twitter_prompt = PromptTemplate(
    template='Generate me twitter post on: {topic}',
    input_variables=['topic']
)

linkedin_prompt = PromptTemplate(
    template='Generate me linkedin post on: {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = RunnableParallel({
    "twitter": RunnableSequence(twitter_prompt, model, parser),
    "linkedin": RunnableSequence(linkedin_prompt, model, parser)
})

result = chain.invoke({ 'topic': 'AI'})
print(result)
