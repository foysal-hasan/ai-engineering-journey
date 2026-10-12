from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

prompt = PromptTemplate(
    template="""
    Generate 5 interesting facts about {topic}
    """,
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = prompt | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({ "topic": "cricket"})
print(result)
