from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)

local_assistant: Agent = Agent(
    name="Local Assistant",
    instructions="You are a helpful assistant running locally.",
    model=external_model,
)

result = Runner.run_sync(local_assistant, "What's the capital of France?")

print(result.final_output)
