import streamlit as st
import folium 
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Google Sheet URL
sheet_url = "https://docs.google.com/spreadsheets/d/1fC354qoKCC847OFmI9p32evXxcCCw_FPvzx9CkhGsVk/edit?usp=sharing"

@st.cache
def load_data(url):
    # Extract the sheet ID from the URL
    url_1 = url.replace("/edit?usp=sharing", "/export?format=csv")
    data = pd.read_csv(url_1)
    return data

# Load the data
data = load_data(sheet_url)

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

# Expanded job database with more locations
job_database = data


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
        
        # Add markers for each matched job with clustering
        marker_cluster = MarkerCluster().add_to(map)
        for job, details in matched_jobs.items():
            folium.Marker(
                location=details['location'],
                popup=f"<strong>{job}</strong><br>Skills: {', '.join(details['skills'])}",
                tooltip=job,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)
        
        # Display the map in Streamlit
        folium_static(map)
    else:
        st.write("Sorry, no volunteer jobs found matching your skillsets and location. Please try another location or check back later!")


# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')


