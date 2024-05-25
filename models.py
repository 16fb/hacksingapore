# models.py

class UserProfile:
    def __init__(self, username, date_of_birth, residential_area, occupation, volunteer_interests, skills):
        self.username = username
        self.date_of_birth = date_of_birth
        self.residential_area = residential_area
        self.occupation = occupation

        type(volunteer_interests)
        volunteer_interests

        # Ensure volunteer interests are joined by a comma and space if it's a list
        self.volunteer_interests = ', '.join(volunteer_interests)
        
        # Ensure skills are joined by a comma and space if it's a list
        self.skills = ', '.join(skills)

    def display_profile(self):
        profile_details = (
            f"Username: {self.username}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Residential Area: {self.residential_area}\n"
            f"Occupation: {self.occupation}\n"
            f"Volunteer Interests: {self.volunteer_interests}\n"
            f"Skills: {self.skills}"
        )
        return profile_details

