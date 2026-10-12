from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-4o-mini")
str_parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['postive', 'negative'] = Field(description='Give the sentiment of the feedback')

feedback_parser = PydanticOutputParser(pydantic_object=Feedback)

classify_prompt = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative\n{feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': feedback_parser.get_format_instructions()}
)

classify_chain = classify_prompt | model | feedback_parser
# result = classify_chain.invoke({ 'feedback': 'This is a terriable smartphone' })
# print(result)


positive_prompt = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback' ]
)

negative_prompt = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback' ]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_prompt | model | str_parser),
    (lambda x: x.sentiment == 'negative', negative_prompt | model | str_parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classify_chain | branch_chain
chain.get_graph().print_ascii()
result = chain.invoke({ 'feedback': 'This is a terriable smartphone' })
print(result)
