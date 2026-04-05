# https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
# Open AI API key is stored in environment variable OPENAI_API_KEY

from openai import OpenAI

def ask_chat_gpt(user_natural_text_query: str, database_schema: list[str]):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Translate this query into SQLite syntax: {user_natural_text_query}. For context"
              f"the following is the relevant schema for the related database. {database_schema}."
    )
    return response.output_text
