# https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
# Open AI API key is stored in environment variable OPENAI_API_KEY

from openai import OpenAI

def ask_LLM(user_natural_text_query: str, database_schema: list[str]):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Convert this query into SQL syntax: {user_natural_text_query}. You may ONLY use fields"
              f"or columns listed in the database schema: {database_schema}. Do not include any additional formatting."
              f"The query will be passed into cur.execute(modify_db_sql_command)."
    )
    return response.output_text