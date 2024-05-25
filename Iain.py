import streamlit as st
import folium 
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from streamlit_gsheets import GSheetsConnection
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# Google Sheet URL
url = "https://docs.google.com/spreadsheets/d/1fC354qoKCC847OFmI9p32evXxcCCw_FPvzx9CkhGsVk/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols = [1,2,3,4,5,6])

#st.dataframe(data)

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
    ['Graphic Design', 'Web Development', 'Event Coordination', 'Marketing', 'Medical Knowledge', 'Customer Service', 'Bilingual', 'Programming', 'Writing']
)

# Job database with exact locations
job_database = data

#print(job_database)

# Function to get coordinates from location
def geocode_location(address):
    geolocator = Nominatim(user_agent="kindhearts_connect")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Button to search for volunteer jobs
if st.button('Search'):
    user_location = geocode_location(location)
    if user_location:
        # Filter jobs based on selected skills and proximity
        matched_jobs = {job: details for job, details in job_database.items() if any(skill in skills for skill in details['skills'])}
        nearby_jobs = {job: details for job, details in matched_jobs.items() if geodesic(user_location, details['location']).km <= 10}  # 10 km radius

        # Check if there are jobs available
        if nearby_jobs:
            st.subheader('Available Volunteer Jobs Near You:')
            for job in nearby_jobs:
                st.write(f"● {job}")
            
            # Create a map centered at the user's location
            map = folium.Map(location=user_location, zoom_start=12)
            
            # Add markers for each nearby job with clustering
            marker_cluster = MarkerCluster().add_to(map)
            for job, details in nearby_jobs.items():
                folium.Marker(
                    location=details['location'],
                    popup=f"<strong>{job}</strong><br>Skills: {', '.join(details['skills'])}",
                    tooltip=job,
                    icon=folium.Icon(color='blue', icon='info-sign')
                ).add_to(marker_cluster)
            
            # Display the map in Streamlit
            folium_static(map)
        else:
            st.write("Sorry, no volunteer jobs found matching your skillsets and location within 10 km. Please try another location or check back later!")
    else:
        st.write("Invalid location. Please enter a valid address.")

# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
