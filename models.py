# models.py

class UserProfile:
    def __init__(self, username, date_of_birth, residential_area, occupation, volunteer_interests, skills):
        self.username = username
        self.date_of_birth = date_of_birth
        self.residential_area = residential_area
        self.occupation = occupation

        #print(type(volunteer_interests))
        #print(volunteer_interests)
        self.volunteer_interests = volunteer_interests
        
        self.skills = skills

    def display_profile(self):
        profile_details = (
            f"Username: {self.username}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Residential Area: {self.residential_area}\n"
            f"Occupation: {self.occupation}\n"
            f"Volunteer Interests: {', '.join(self.volunteer_interests)}\n"
            f"Skills: {', '.join(self.skills)}"
        )
        return profile_details

