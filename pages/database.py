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
        # Ensure the data is joined as a string if it's a list
        volunteer_interests_str = ', '.join(user.volunteer_interests) if isinstance(user.volunteer_interests, list) else user.volunteer_interests
        skills_str = ', '.join(user.skills) if isinstance(user.skills, list) else user.skills
        cursor.execute(
            "INSERT INTO users (username, date_of_birth, residential_area, occupation, volunteer_interests, skills) VALUES (?, ?, ?, ?, ?, ?)",
            (user.username, user.date_of_birth, user.residential_area, user.occupation, volunteer_interests_str, skills_str)
        )
        conn.commit()

def get_user_profile(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = cursor.fetchone()
    if data:
        # No additional string manipulation is required here
        return UserProfile(
            username=str(data[1]), 
            date_of_birth=str(data[2]), 
            residential_area=str(data[3]),
            occupation=str(data[4]), 
            volunteer_interests=str(data[5]),  # Directly pass the string
            skills=str(data[6])               # Directly pass the string
        )
    return None

