from llama_index import LLM
from few_shot_examples import few_shot_examples

def generate_sql(natural_language_query):
    # Instantiate the LLaMA model
    model = LLM(model='LLaMA')

    prompt = f"Translate the following question into SQL: {natural_language_query}\nExamples:\n{few_shot_examples}"
    
    try:
        sql_query = model.generate(prompt)
        return sql_query
    except Exception as e:
        return f"Error: {str(e)}"

