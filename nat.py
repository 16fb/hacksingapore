import streamlit as st
import folium 
from streamlit_folium import folium_static


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

job_database = {
    "Beach Cleanup - East Coast Park": {"skills": ["Environmental Conservation"], "location": (1.3039, 103.9123)},
    "Community Library Helper - Central Library": {"skills": ["Teaching", "Mentoring"], "location": (1.2905, 103.8468)},
    "Elderly Care Companion - West Haven": {"skills": ["Elderly Care", "First Aid"], "location": (1.3521, 103.8198)}
}

# Button to search for volunteer jobs
if st.button('Search'):
    # Filter jobs based on selected skills
    matched_jobs = {job: details for job, details in job_database.items() if any(skill in skills for skill in details['skills'])}
    
    # Check if there are jobs available
    if matched_jobs:
        st.subheader('Available Volunteer Jobs Near You:')
        for job in matched_jobs:
            st.write(f"● {job}")
        
        # Create a map centered at the first job's location
        first_job_location = list(matched_jobs.values())[0]['location']
        map = folium.Map(location=first_job_location, zoom_start=12)
        
        # Add markers for each matched job
        for job, details in matched_jobs.items():
            folium.Marker(
                location=details['location'],
                popup=job,
                tooltip=job
            ).add_to(map)
        
        # Display the map in Streamlit
        folium_static(map)
    else:
        st.write("Sorry, no volunteer jobs found matching your skillsets and location. Please try another location or check back later!")


# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
