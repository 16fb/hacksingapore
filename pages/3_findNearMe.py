import streamlit as st
import folium 
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from streamlit_gsheets import GSheetsConnection
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from database import insert_user_profile, get_user_profile, setup_database


# Google Sheet URL
url = "https://docs.google.com/spreadsheets/d/1fC354qoKCC847OFmI9p32evXxcCCw_FPvzx9CkhGsVk/edit?usp=sharing"
#url = "https://docs.google.com/spreadsheets/d/1V1M7Hy0yyrPGiX-mzdB-N6IE-BnMwNR2-sfE8zdTHgQ/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols = [1,2,3,4,5,6,7,8])

st.dataframe(data)

#Logo
st.image('image\Logo.jpg', width=200, use_column_width="never")


# Display a welcome message
st.header('Welcome to KindHearts Connect!')
st.write('Find volunteering opportunities near you and make a difference in your community.')

# Search box to enter the location
search_username = st.text_input('Enter your Username:', '')

# Search box to enter the location
location = st.text_input('Enter your location to find volunteer jobs nearby:', '')

# Function to get coordinates from location
def geocode_location(address):
    geolocator = Nominatim(user_agent="kindhearts_connect")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
    
def geocode_locationPostal(address):
    geolocator = Nominatim(user_agent="kindhearts_connect")
    location = geolocator.geocode({"country":"sg", "postalcode":address})
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Multi-select box to enter the skillsets

### Goals
# pandas dataframe convert to specific dictionary/json

#print(type(data)) # pandas DataFrame
#print("Data formatting") 
#print(data) # pandas DataFrame
#print(data.dtypes) # Every column is an object
#print(data.skills)
#print(data.location)






# Button to search for volunteer jobs
if st.button('Search'):
    final_dict = {}

    for index, row in data.iterrows():
        #print(row["name"], row["date"], row["address"], row["location"], row["shift"], row["skills"])
        #print(row["name"], row["skills"], row["location"])

        ## extract string of 2 floats into tuples
        location_helps = geocode_locationPostal(row["postalCode"])
        print(location_helps)

        ## extract string of skills into list
        skillss = []
        for item in row["skills"].split(','):
            skillss.append(item)

        final_dict[ str(row["name"]) ] = {
                        "skills": skillss,
                        "location": location_helps
                    }


    # Converting data from 
    job_database = final_dict
    print(job_database)

    #print(job_database["Mobile Photography in Nature [Y-Y-T]"])

    profile = get_user_profile(search_username)
    if profile:
        # Direct display of the profile information without alteration
        st.text(profile.display_profile())

        skills = profile.skills

        user_location = geocode_location(location)
        print(user_location)
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
    else:
        st.error("Profile not found.")

    

# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
