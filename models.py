import sqlite3

DB_NAME = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_prompt TEXT,
            pine_script TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_history(user_prompt, pine_script):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO history (user_prompt, pine_script) VALUES (?, ?)", 
              (user_prompt, pine_script))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, user_prompt FROM history ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

def get_script_by_id(script_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT pine_script FROM history WHERE id=?", (script_id,))
    data = c.fetchone()
    conn.close()
    return data[0] if data else None
