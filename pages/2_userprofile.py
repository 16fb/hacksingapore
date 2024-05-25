import streamlit as st
from database import insert_user_profile, get_user_profile
from models import UserProfile

volunteer_interests_options = [
    "Environmental Conservation", "Animal Welfare", "Cooking", "Elderly Care", "Tutoring",
    "First Aid", "Technical Support", "Fund Raising", "Child Care", "Event Planning",
    "Photography", "Mentoring"
]

skills_options = [
    "Project Management", "Public Speaking", "Data Analysis", "Graphic Design", "Web Development",
    "Medical Knowledge", "Marketing", "Writing", "Customer Service", "Bilingual", "Programming",
    "Event Coordination"
]

st.title('User Profile Page')

with st.form("user_form"):
    st.write("Create a new user profile:")
    username = st.text_input("Username")
    date_of_birth = st.date_input("Date of Birth")
    residential_area = st.text_input("Residential Area")
    occupation = st.text_input("Occupation")
    volunteer_interests = st.multiselect("Volunteer Interests", volunteer_interests_options, default=None)
    skills = st.multiselect("Skills", skills_options, default=None)
    submitted = st.form_submit_button("Save")
    if submitted:
        user = UserProfile(username, date_of_birth, residential_area, occupation, volunteer_interests, skills)
        insert_user_profile(user)
        st.success("Profile created successfully!")

search_username = st.text_input("Search Username")
if st.button("Search"):
    profile = get_user_profile(search_username)
    if profile:
        st.write(profile.display_profile())
    else:
        st.error("Profile not found.")
