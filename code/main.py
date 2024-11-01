from flask import Flask, request, jsonify
from llm import generate_sql
from database import execute_query

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json['query']
    sql_query = generate_sql(user_query)
    
    if sql_query.startswith("Error"):
        return jsonify({"error": sql_query}), 400
    
    result = execute_query(sql_query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

