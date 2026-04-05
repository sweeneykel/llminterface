# https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
# Open AI API key is stored in environment variable OPENAI_API_KEY

from openai import OpenAI

def ask_LLM(user_natural_text_query: str, database_schema: list[str]):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Translate the following query into SQLite syntax: {user_natural_text_query}. For context"
              f"the following is the relevant schema for the related database. {database_schema}. Also, the query"
              f"will be passed through the command cur.execute(modify_db_sql_command) and therefore should not have"
              f"any additional formatting."
    )
    return response.output_text