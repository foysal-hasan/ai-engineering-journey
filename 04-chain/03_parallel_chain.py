from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI


load_dotenv(override=True)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

parallel_chain = RunnableParallel({
        'notes': prompt1 | model | parser,
        'quiz': prompt2 | model | parser
})

output_chain = prompt3 | model | parser

chain = parallel_chain | output_chain
chain.get_graph().print_ascii()
result = chain.invoke({
    "text": """
Models

LLMs are powerful AI tools that can interpret and generate text like humans. They’re versatile enough to write content, translate languages, summarize, and answer questions without needing specialized training for each task.
In addition to text generation, many models support:
 Tool calling - calling external tools (like databases queries or API calls) and use results in their responses.
 Structured output - where the model’s response is constrained to follow a defined format.
 Multimodality - process and return data other than text, such as images, audio, and video.
 Reasoning - models perform multi-step reasoning to arrive at a conclusion.
Models are the reasoning engine of agents. They drive the agent’s decision-making process, determining which tools to call, how to interpret results, and when to provide a final answer.
The quality and capabilities of the model you choose directly impact your agent’s baseline reliability and performance. Different models excel at different tasks - some are better at following complex instructions, others at structured reasoning, and some support larger context windows for handling more information.
LangChain’s standard model interfaces give you access to many different provider integrations, which makes it easy to experiment with and switch between models to find the best fit for your use case.
For provider-specific integration information and capabilities, see the provider’s chat model page.
LangSmith traces each model call so you can compare providers, inspect tool routing, and debug failures. Follow the tracing quickstart to get set up.
We recommend you also set up LangSmith Engine which monitors your traces, detects issues, and proposes fixes.
​
Basic usage
Models can be utilized in two ways:
With agents - Models can be dynamically specified when creating an agent.
Standalone - Models can be called directly (outside of the agent loop) for tasks like text generation, classification, or extraction without the need for an agent framework.
The same model interface works in both contexts, which gives you the flexibility to start simple and scale up to more complex agent-based workflows as needed.
"""
})

print(result)


