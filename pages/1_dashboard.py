import streamlit as st
from database import insert_user_profile, get_user_profile, setup_database

# Mock user data
user_activities = [
    {"date": "2024-06-15", "activity": "Participated in local park cleanup", "hours": 2},
    {"date": "2024-06-10", "activity": "Assisted in web development for non-profit", "hours": 3},
    {"date": "2024-06-05", "activity": "Conducted workshop on first aid", "hours": 1.5},
]

user_achievements = [
    {"name": "Volunteer of the Month", "date": "May 2024"},
    {"name": "100 Hours Milestone", "date": "June 2024"},
]

user_badges = [
    {"name": "Eco Warrior", "icon": "🌍"},
    {"name": "Tech Guru", "icon": "💻"},
]


st.title('Volunteer Dashboard')

st.write("Enter a username to display the profile:")

search_username = st.text_input("Search Username")
if st.button("Search"):

    profile = get_user_profile(search_username)
    if profile:
        # Direct display of the profile information without alteration
        st.text(profile.display_profile())
        
        # Display the user profile and stats
        st.header('User Profile and Stats')
        st.write("Welcome back,", profile.username, "!!!")

        # Display User Activities
        st.subheader('Recent Activities')
        for activity in user_activities:
            st.text(f"{activity['date']}: {activity['activity']} ({activity['hours']} hours)")

        # Display Achievements
        st.subheader('Achievements')
        for achievement in user_achievements:
            st.text(f"{achievement['date']}: {achievement['name']}")

        # Display Badges
        st.subheader('Badges Earned')
        for badge in user_badges:
            st.text(f"{badge['icon']} {badge['name']}")

    else:
        st.error("Profile not found.")


st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")


st.markdown('---')
st.write('Thank you for making a difference with your volunteer work!')
