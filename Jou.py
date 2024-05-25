import streamlit as st

# Title of the app
st.title('KindHearts Connect')

# Display a welcome message
st.header('Welcome to KindHearts Connect!')
st.write('Find volunteering opportunities near you and make a difference in your community.')

# Search box to enter the location
location = st.text_input('Enter your location to find volunteer jobs nearby:', '')

# Button to search for volunteer jobs
if st.button('Search'):
    # For demonstration, assuming we have a function that fetches jobs based on location
    # This should be replaced with actual logic to fetch data
    jobs = ["Beach Cleanup - East Coast Park", "Community Library Helper - Central Library", "Elderly Care Companion - West Haven"]
    
    # Check if there are jobs available
    if jobs:
        st.subheader('Available Volunteer Jobs Near You:')
        for job in jobs:
            st.write(f"● {job}")
    else:
        st.write("Sorry, no volunteer jobs found near this location. Please try another location or check back later!")

# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
