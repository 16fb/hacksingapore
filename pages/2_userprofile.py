import streamlit as st
from database import insert_user_profile, get_user_profile, setup_database
from models import UserProfile
import sqlite3

# Assuming you have a database connection set up
conn = sqlite3.connect('volunteer.db', check_same_thread=False)
c = conn.cursor()


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
    "Programming",
    "First Aid",
    "Marketing",
    "Customer Service",
    "Bilingual",
    "Cooking",
    "Sign Language"
]

# Streamlit interface for creating and viewing user profiles

#Logo
st.image('image\Logo.jpg', width=200, use_column_width="never")

#Display welcome
st.header('Welcome to KindHearts Connect!')

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
        print("Volunteer Interests:", volunteer_interests)  # Check what is being passed
        print("Skills:", skills)  # Check what is being passed

st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")
