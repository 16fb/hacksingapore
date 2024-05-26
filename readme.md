## KindHearts Connects
### General Aim
Addresses low volunteerism rates in Singapore with our web app. <br>
Simplifying the process of finding and engaging in volunteer activities. <br>
Help users discover opportunities based on their interests, skills, and location. <br>
Features a straightforward application process, encouraging ease of user pickup and interest. <br>

### Demo Video Link
https://youtu.be/temHMRVEq50?si=erwKsK_x-M6XqjFk <br>

### Future Ideas
Skills development workshops and networking features to enhance volunteer engagement and community impact <br>

## Usage and Technical Information
### Technical Gist
Web application built using streamlit, a python module. <br>
Google Sheet used as storage of volunteer events. Mimicks an eventual API database used by volunteer.gov.sg <br>
Google Forms populates Google Sheets. <br>
Internal database uses a sqlite3 database, store user information and preferences. <br>
User's location and skills and preferences, are analysed against event's information and requirements. <br> 
User's locations coordinates identified using a Singapore Postal Code, used to identify events within 10km. <br>

### Quick-Start
Streamlit is a python module, so use it as `py -m pip install streamlit` <br>
Then to run an example streamlit `py -m streamlit hello`<br>
Then to run the specific file `py -m streamlit run app.py`<br>

### additional pip modules to install
- streamlit
- streamlit_folium
- folium
- st-gsheets-connection
- geopy
- sqlite3
 


