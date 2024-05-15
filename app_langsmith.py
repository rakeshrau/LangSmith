from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please resposne to the user request only based on the given context"),
        ("user","Question:{question}\nContext:{context}")


    ]


)
model=ChatOpenAI(model="gpt-4")
output_parser=StrOutputParser()

chain=prompt|model|output_parser
question="Can you summarize the speech?"
context=""" Life is a precious gift. It is the sum of one's work, journey, dreams, joys, sorrows, successes, and battles for change. Life is more of a journey than a destination. It must be lived peacefully and happily. Seeking the meaning and purpose of life is the biggest search in the life of a man, and the questions about the meaning of human life are age-old. Life, however, still has some attractive elements, offering one a ray of hope and positivity, each passing day.
We have individuals, families, relatives, and friends who make our lives unique, worth living, and make us feel that our lives are special. Our lives are challenging, but those challenges are what make it worth living."""

print(chain.invoke({"question":question,"context":context}))