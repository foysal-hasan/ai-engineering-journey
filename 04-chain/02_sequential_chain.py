from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

report_prompt = PromptTemplate(
    template="""
    generate me a detailed report on {topic}
    """,
    input_variables=['topic']
)

summary_prompt = PromptTemplate(
    template="""
    Generate me 5 pointer summary from the "{text}"
    """,
    input_variables=['text']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = report_prompt | model | parser | summary_prompt | model | parser

result = chain.invoke({ 'topic': 'unemployment in bangladesh'})
print(result)