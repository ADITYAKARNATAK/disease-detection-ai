import sqlite3
from datetime import datetime


DB_NAME = "database.db"


def create_db():

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    c.execute("""

    CREATE TABLE IF NOT EXISTS history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symptoms TEXT,

        report_text TEXT,

        result TEXT,

        date_time TEXT

    )

    """)

    conn.commit()
    conn.close()



def insert_data(symptoms, text, result):

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute("""

    INSERT INTO history
    (symptoms, report_text, result, date_time)

    VALUES (?, ?, ?, ?)

    """, (symptoms, text, result, now))

    conn.commit()
    conn.close()



def get_history():

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    c.execute("SELECT * FROM history")

    data = c.fetchall()

    conn.close()

    return data