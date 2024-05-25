import streamlit as st
import sqlite3
import pandas as pd
import folium
from streamlit_folium import st_folium

# Database connection
conn = sqlite3.connect('volunteer.db', check_same_thread=False)
c = conn.cursor()

def setup_database():
    # Create tables for jobs, users, preferences if they don't exist
    with conn:
        c.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                location TEXT,
                description TEXT,
                latitude REAL,
                longitude REAL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                interests TEXT,
                skills TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS preferences (
                user_id INTEGER,
                preferred_location TEXT,
                interests TEXT,
                skills TEXT,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')

setup_database()

def fetch_jobs(location):
    c.execute("SELECT * FROM jobs WHERE location LIKE ?", ('%'+location+'%',))
    return c.fetchall()

def insert_dummy_data():
    with conn:
        c.execute("INSERT INTO jobs (title, location, description, latitude, longitude) VALUES (?, ?, ?, ?, ?)",
                  ("Beach Cleanup", "East Coast Park", "Help clean up the beach.", 1.3521, 103.8198))

# Uncomment below to insert dummy data once
# insert_dummy_data()

st.title('KindHearts Connect')

location = st.text_input('Enter your location:', '')
jobs = []  # Define jobs here to ensure scope includes the map section

if st.button('Find Volunteer Opportunities'):
    jobs = fetch_jobs(location)
    if jobs:
        st.subheader('Volunteer Opportunities Near You')
        for job in jobs:
            st.write(f"{job[1]} at {job[2]} - {job[3]}")
    else:
        st.write("No jobs found. Try a different location.")

# Map display
if jobs:
    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12)
    for job in jobs:
        folium.Marker(
            [job[4], job[5]],
            popup=f"{job[1]}: {job[3]}",
            tooltip=job[1]
        ).add_to(map)
    st_folium(map, width=725)

st.write('Connect with friends who are also interested!')
# Placeholder for social features
# Implement using user IDs and a system to track event sign-ups

# User preference settings (simplified)
with st.form("user_preferences"):
    st.write("Your Preferences")
    username = st.text_input("Username")
    interests = st.text_area("Enter your interests")
    skills = st.text_area("Enter your skills")
    if st.form_submit_button("Save Preferences"):
        with conn:
            c.execute("INSERT INTO users (username, interests, skills) VALUES (?, ?, ?)",
                      (username, interests, skills))
            conn.commit()
        st.success("Preferences saved!")

st.write('KindHearts Connect © 2024')
