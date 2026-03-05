from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)

gemini_assistant: Agent = Agent(
    name="Gemini Assistant",
    instructions="You are a helpful assistant. Keep responses concise.",
    model=external_model,
)

result = Runner.run_sync(
    gemini_assistant, "Explain what an AI agent is in one sentence."
)

print(result.final_output)
