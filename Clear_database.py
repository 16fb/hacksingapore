import sqlite3

def clear_table(table_name):
    conn = sqlite3.connect('volunteer.db')
    cursor = conn.cursor()
    query = f"DELETE FROM {table_name};"
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(f"All records from {table_name} have been deleted.")

# Usage example:
clear_table('users')
