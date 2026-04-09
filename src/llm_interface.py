# https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
# Open AI API key is stored in environment variable OPENAI_API_KEY

from openai import OpenAI

def ask_llm(user_natural_text_query: str, database_schema: dict):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Convert this query into SQL syntax: {user_natural_text_query}. This is the database schema:"
              f"Keys are table names and values are a list of column names {database_schema}. "
              f"Do not include any additional formatting.The query will be passed as an argument cur.execute()."
    )
    return response.output_text