from dotenv import load_dotenv
from agents import Agent, Runner
from openai import AsyncOpenAI
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from os import getenv

load_dotenv()

gemini_api: None | str = getenv("GEMINI_API_KEY")

gemini_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=gemini_client
)

assistant: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant who gives brief, friendly responses.",
    model=gemini_model,
)

result = Runner.run_sync(assistant, "Hello! What can you help me with today?")

print(result.final_output)
