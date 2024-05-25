import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

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
    ["Project Management",
    "Public Speaking",
    "Programming",
    "First Aid",
    "Marketing",
    "Customer Service",
    "Bilingual",
    "Cooking",
    "Sign Language"
    ]
)


# Job database with exact locations
job_database = {
    "Mobile Photography in Nature [Y-Y-T]": {"skills": ["Graphic Design", "Web Development"], "location": (1.4405739802247404, 103.73564417585078)},
    "[E3] Our Tampines Hub Festival": {"skills": ["Event Coordination"], "location": (1.353308328096193, 103.94089296047616)},
    "[E6] Community Championship 3x3 Basketball Challenge": {"skills": ["Event Coordination"], "location": (1.3271361451249875, 103.93328656997474)},
    "[TN5] BAS Youth Cup 2024": {"skills": ["Event Coordination"], "location": (1.3211952858158384, 103.88785806306707)},
    "[TN5] KOTC Asia League Circuit 3 (Basketball)": {"skills": ["Marketing"], "location": (1.3202623237084459, 103.84472909141088)},
    "[TN5] Squash - Pesta Sukan 2024": {"skills": ["Event Coordination"], "location": (1.3056343991703967, 103.88090788906455)},
    "Re:ground @ Dungeon - Tranquil Ties [TRB]": {"skills": ["Event Coordination"], "location": (1.3007360214142216, 103.83761584723872)},
    "Project Sort It Out - SORT Walk and Workshop [YCLPA]": {"skills": ["Event Coordination"], "location": (1.3403732884907542, 103.70515493559607)},
    "[E1] ActiveSG Water Polo Cup 2024": {"skills": ["Bilingual"], "location": (1.3403089330888962, 103.70497254539693)},
    "[TN5] Handball - Pesta Sukan 2024": {"skills": ["Bilingual"], "location": (1.331820392821176, 103.72119410440554)},
    "Healthy with KidSTART Distribution (June 2024)": {"skills": ["Medical Knowledge"], "location": (1.3127132147994065, 103.8373549896772)},
    "[C5] Swimming Volunteer for Special Olympics (Jul - Dec 24)": {"skills": ["Bilingual"], "location": (1.3109954205477847, 103.76668076813452)},
    "[C4] Play-ability - Basketball (ASD) [Jul - Sep] 2024": {"skills": ["Bilingual"], "location": (1.3109954205477847, 103.76668076813452)},
    "Hearts Connect @ SAS - 4 July 2024 [BSV]": {"skills": ["Customer Service", "Bilingual"], "location": (1.367995, 103.892185)},
    "[C4] Play-ability - Soundball Singapore [Jul - Sep] 2024": {"skills": ["Bilingual"], "location": (1.31907, 103.82511)},
    "[C4] Play-ability - Basketball (Touch BM) [Jul - Sep] 2024": {"skills": ["Bilingual"], "location": (1.290363, 103.826905)},
    "Book Distribution (13 & 14 June 2024)": {"skills": ["Marketing", "Writing"], "location": (1.29807, 103.8498)},
    "Child Protective Service Online Info Sharing Session": {"skills": ["Programming", "Event Coordination"], "location": (1.3403089330888962, 103.70497254539693)},
    "Le Ho Bho 2024 instructor recruitment [Y-Y]": {"skills": ["Bilingual"], "location": (1.3007360214142216, 103.83761584723872)},
    "[TN5] Flying Disc - Pesta Sukan 2024": {"skills": ["Event Coordination"], "location": (1.36921, 103.85634)},
}

print(job_database["Mobile Photography in Nature [Y-Y-T]"])

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

# Some extra information or links can be added here
st.write('Volunteer today and be the change you want to see!')
st.markdown("[Learn more about volunteering](https://www.example.com)")

# Footer
st.write('KindHearts Connect © 2024')
