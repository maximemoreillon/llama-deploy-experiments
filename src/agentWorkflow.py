from llama_index.core.agent.workflow import (
    AgentWorkflow,
    FunctionAgent,
    ReActAgent,
)
from llama_index.core.tools import FunctionTool
import asyncio
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

load_dotenv()

# Define some tools
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


# Create agent configs
# NOTE: we can use FunctionAgent or ReActAgent here.
# FunctionAgent works for LLMs with a function calling API.
# ReActAgent works for any LLM.
calculator_agent = FunctionAgent(
    name="calculator",
    description="Performs basic arithmetic operations",
    system_prompt="You are a calculator assistant.",
    tools=[
        FunctionTool.from_defaults(fn=add),
        FunctionTool.from_defaults(fn=subtract),
    ],
    llm=OpenAI(model="gpt-4"),
)

retriever_agent = FunctionAgent(
    name="retriever",
    description="Manages data retrieval",
    system_prompt="You are a retrieval assistant.",
    llm=OpenAI(model="gpt-4"),
)

# Create and run the workflow
agentWorkflow = AgentWorkflow(
    agents=[calculator_agent, retriever_agent], root_agent="calculator"
)


async def main():
    response = await agentWorkflow.run(user_msg="Can you add 5 and 3?")

    print(response)


# Make this script runnable from the shell so we can test the workflow execution
if __name__ == "__main__":
    asyncio.run(main())


