import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

if tavily_api_key is None:
    raise ValueError("TAVILY_API_KEY not found in .env file")

tavily_client = TavilyClient(api_key=tavily_api_key)
response = tavily_client.search("Who is Leo Messi?")

print(response)