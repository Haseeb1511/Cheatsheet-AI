from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["math.py"],
                "transport": "stdio"
            },
            "weather":{
                "url": "http://127.0.0.1:8000",
                "transport": "streamable-http"
            }
         })

    tools=await client.get_tools()
    model=ChatOpenAI(model="gpt-4.1-nano")
    agent=create_react_agent(model,tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    weather_response = await agent.ainvoke(
    {"messages":[{"role":"user","content":"what is weather of newyork"}]})

    print("Math response:", math_response['messages'][-1].content)
    print("Weather response:", weather_response['messages'][-1].content)


asyncio.run(main())