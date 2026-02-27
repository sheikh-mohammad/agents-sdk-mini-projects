from agents import Agent, Runner
from dotenv import load_dotenv
from os import getenv
from openai import AsyncOpenAI
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

load_dotenv()

gemini_api = getenv("GEMINI_API_KEY")

gemini_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

gemini_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=gemini_client
)

fast_assistant: Agent = Agent(
    name="Fast Assistant", instructions="You are a quick helper.", model=gemini_model
)

result = Runner.run_sync(
    fast_assistant,
    "What's 2 + 2?"
)

print(result.final_output)