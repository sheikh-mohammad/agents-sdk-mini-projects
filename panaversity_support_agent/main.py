from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import chainlit as cl
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")

gemini_client = AsyncOpenAI(
    api_key=gemini_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=gemini_client
)

config = RunConfig(
    model=gemini_model, model_provider=gemini_client, tracing_disabled=True
)

agent = Agent(
    name="Panaversity Support Agent",
    instructions="You are a helpful assistant that can answer questions and tasks.",
)


@cl.on_chat_start
async def first_message():

    await cl.Message(
        content="Hello! I'm Panaversity Support Agent. How can I help you today?"
    ).send()


@cl.on_message
async def chat(message: cl.Message):

    result = await Runner.run(agent, input=message.content, run_config=config)

    await cl.Message(content=result.final_output).send()
