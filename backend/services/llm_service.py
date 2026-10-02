import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def get_llm_response(query: str) -> str:
    print("query ", query)

    prompt = f"""
    You are a helpful assistant.
    Please answer the following question clearly and in a structured way:

    {query}
    """

    response = await client.aio.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text