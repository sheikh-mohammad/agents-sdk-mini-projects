from agents import Agent, Runner
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key: str | None = os.getenv("GEMINI_API_KEY")

gmail_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

gemini_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=gmail_client
)

agent: Agent = Agent(
    name="Assistant", instructions="You are a helpful assistant", model=gemini_model
)

result = Runner.run_sync(agent, "Hello! What can you help me with today?")

print(result.final_output)