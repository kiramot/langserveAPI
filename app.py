from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

# Set the OPENAI_API_KEY environment variable
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize the FastAPI application
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

# Initialize the ChatOpenAI model
model = ChatOpenAI()

# Define prompts for essay and poem generation
essay_prompt = ChatPromptTemplate.from_template("provide me an essay about {topic}")
poem_prompt = ChatPromptTemplate.from_template("provide me an poem about {topic}")

# Add routes for different endpoints
add_routes(app, model, path="/openai")
add_routes(app, essay_prompt | model, path="/essay")
add_routes(app, poem_prompt | model, path="/poem")

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
