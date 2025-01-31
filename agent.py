from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import sys
import json
import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")


async def main(input_data):
    productName = input_data.get("productName")

    task = f"Navigate to only 2 different store websites that are selling the {productName}. On each website, collect the total number of reviews, and the average review rating. Output the sum of the number of reviews from each page and the total average of reviews you can find."

    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    
    print(result)

if __name__ == "__main__":
    input_data = sys.stdin.read()
    
    try:
        parsed_data = json.loads(input_data)
        asyncio.run(main(parsed_data))
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON input"}))