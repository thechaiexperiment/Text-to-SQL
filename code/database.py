import sqlite3

def execute_query(sql_query):
    connection = sqlite3.connect('database.db')  # Specify your database name
    cursor = connection.cursor()

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result if result else {"message": "No results found."}
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()

