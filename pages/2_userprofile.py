import streamlit as st
from database import insert_user_profile, get_user_profile, setup_database
#from models import UserProfile
import sqlite3

# Assuming you have a database connection set up
conn = sqlite3.connect('volunteer.db', check_same_thread=False)
c = conn.cursor()

class UserProfile:
    def __init__(self, username, date_of_birth, residential_area, occupation, volunteer_interests, skills):
        self.username = username
        self.date_of_birth = date_of_birth
        self.residential_area = residential_area
        self.occupation = occupation
        self.volunteer_interests = ''.join(volunteer_interests)  # Store as a single string
        self.skills = ''.join(skills)  # Store as a single string

    def display_profile(self):
        profile_details = (
            f"Username: {self.username}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Residential Area: {self.residential_area}\n"
            f"Occupation: {self.occupation}\n"
            f"Volunteer Interests: {self.volunteer_interests}\n"
            f"Skills: {self.skills}"
        )
        return profile_details

# Function to insert a new user profile into the database
def insert_user_profile(user):
    with conn:
        c.execute(
            "INSERT INTO users (username, date_of_birth, residential_area, occupation, volunteer_interests, skills) VALUES (?, ?, ?, ?, ?, ?)",
            (user.username, user.date_of_birth, user.residential_area, user.occupation, user.volunteer_interests, user.skills)
        )
        conn.commit()

# Function to get user profile from database
def get_user_profile(username):
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    if data:
        return UserProfile(*data[1:])  # Unpack all fields except the ID
    return None

# Define a list of volunteer interests
volunteer_interests_options = [
    "Environmental Conservation",
    "Animal Welfare",
    "Cooking",
    "Elderly Care",
    "Tutoring",
    "First Aid", 
    "Technical Support", 
    "Fund Raising",
    "Child Care",
    "Event Planning",
    "Photography",
    "Mentoring"
]

# Define a list of skills
skills_options = [
    "Project Management",
    "Public Speaking",
    "Data Analysis",
    "Graphic Design",
    "Web Development",
    "Medical Knowledge",
    "Marketing",
    "Writing",
    "Customer Service",
    "Bilingual",
    "Programming",
    "Event Coordination"
]

# Streamlit interface for creating and viewing user profiles
st.title('User Profile Page')

with st.form("user_form"):
    st.write("Create a new user profile:")
    username = st.text_input("Username")
    date_of_birth = st.date_input("Date of Birth")
    residential_area = st.text_input("Residential Area")
    occupation = st.text_input("Occupation")
    volunteer_interests = st.multiselect("Volunteer Interests", volunteer_interests_options, default=None)  # Multiselect for volunteer interests
    skills = st.multiselect("Skills", skills_options, default=None)  # Multiselect for skills
    submitted = st.form_submit_button("Save")
    if submitted:
        user = UserProfile(username, date_of_birth, residential_area, occupation, volunteer_interests, skills)
        setup_database()
        insert_user_profile(user)
        st.success("Profile created successfully!")

st.write("Enter a username to display the profile:")

search_username = st.text_input("Search Username")
if st.button("Search"):
    profile = get_user_profile(search_username)
    if profile:
        # Direct display of the profile information without alteration
        st.text(profile.display_profile())
    else:
        st.error("Profile not found.")

