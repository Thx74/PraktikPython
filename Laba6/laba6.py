import sqlite3

def create_database(database_file='my_database.db'):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        age INTEGER
        )
    ''')
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('John Doe', 'john.doe@example.com', 30)")
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('Jane Doe', 'jane.doe@example.com', 25)")
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('Peter Pan', 'peter.pan@example.com', 20)")
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('Peter Pan', 'jane.doe@example.com', 30)")
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('Pan Stepan', 'kokone.exp@example.com', 37)")
    conn.commit()
    conn.close()

def analyze_table(table_name, database_file='my_database.db'):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_names = [row[1] for row in cursor.fetchall()]
    for column_name in column_names:
        cursor.execute(f"SELECT {column_name} FROM {table_name}")
        values = cursor.fetchall()
        value_counts = {}
        for value in values:
            value = value[0]
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
        most_frequent_value = max(value_counts, key=value_counts.get)
        most_frequent_count = value_counts[most_frequent_value]
        print(f"Column: {column_name}")
        print(f"Number of different values: {len(value_counts)}")
        print(f"Most frequent value: {most_frequent_value} ({most_frequent_count} times)")
        print("-" * 20)
    conn.close()

create_database()

analyze_table('users')
