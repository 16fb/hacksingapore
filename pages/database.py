# database.py
import sqlite3
from models import UserProfile

def get_connection():
    return sqlite3.connect('volunteer.db', check_same_thread=False)

def setup_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                date_of_birth TEXT,
                residential_area TEXT,
                occupation TEXT,
                volunteer_interests TEXT,
                skills TEXT
            );
        """)
        conn.commit()

def insert_user_profile(user):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, date_of_birth, residential_area, occupation, volunteer_interests, skills) VALUES (?, ?, ?, ?, ?, ?)",
            (user.username, user.date_of_birth, user.residential_area, user.occupation, user.volunteer_interests, user.skills)
        )
        conn.commit()

def get_user_profile(username):
    conn = get_connection()
    cursor = conn
