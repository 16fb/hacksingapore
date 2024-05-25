import streamlit as st

# Title of the app
st.title('KindHearts Connect')

# Display a welcome message
st.header('Welcome to KindHearts Connect!')
st.write('Find volunteering opportunities near you and make a difference in your community.')

# Search box to enter the location
location = st.text_input('Enter your location to find volunteer jobs nearby:', '')

# Multi-select box to enter the skillsets
skills = st.multiselect(
    'Select your skillsets:',
    ['Teaching', 'Cooking', 'Event Planning', 'First Aid', 'Childcare', 'Elderly Care', 'Environmental Conservation', 'Fundraising', 'Mentoring', 'Technical Support']
)

# Button to search for volunteer jobs
if st.button('Search'):
    # For demonstration, assuming we have a function that fetches jobs based on location and skillsets
    # This should be replaced with actual logic to fetch data
    job_database = {
        "Beach Cleanup - East Coast Park": ["Environmental Conservation"],
        "Community Library Helper - Central Library": ["Teaching", "Mentoring"],
        "Elderly Care Companion - West Haven": ["Elderly Care", "First Aid"]
    }
    
    matched_jobs = [job for job, required_skills in job_database.items() if any(skill in skills for skill in required_skills)]
    
    # Check if there are jobs available
    if matched_jobs:
        st.subheader('Available Volunteer Jobs Near You:')
        for job in matched_jobs:
            st.write(f"● {job}")
    else:
        st.write("Sorry, no volunteer jobs found matching your skillsets and location. Please try another location or check back later!")

# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
