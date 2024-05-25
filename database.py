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
        # Debugging statements to check data before insertion
        print("Volunteer Interests:", user.volunteer_interests)
        print("Skills:", user.skills)
        cursor.execute(
            "INSERT INTO users (username, date_of_birth, residential_area, occupation, volunteer_interests, skills) VALUES (?, ?, ?, ?, ?, ?)",
            (user.username, user.date_of_birth, user.residential_area, user.occupation, ', '.join(user.volunteer_interests), ', '.join(user.skills))
        )
        conn.commit()

def get_user_profile(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = cursor.fetchone()
    if data:
        # Debugging statements to check data right after retrieval
        print("DB Volunteer Interests:", data[5])
        print("DB Skills:", data[6])
        return UserProfile(
            username=str(data[1]), 
            date_of_birth=str(data[2]), 
            residential_area=str(data[3]),
            occupation=str(data[4]), 
            volunteer_interests=str(data[5]).split(", "),
            skills=str(data[6]).split(", ")
        )
    return None
