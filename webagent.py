from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import os

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(
        id="gpt-4o",
        base_url="https://models.inference.ai.azure.com"
    ),
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources",
        "Analyze the search results critically",
        "Present information in a clear and organized manner",
        "Always provide comprehensive and up-to-date information"
    ],
    show_tool_calls=True,
    markdown=True
)

web_agent.print_response("Whats happening in USA?", stream=True)