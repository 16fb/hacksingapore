class UserProfile:
    def __init__(self, username, date_of_birth, residential_area, occupation, volunteer_interests, skills):
        self.username = username
        self.date_of_birth = date_of_birth
        self.residential_area = residential_area
        self.occupation = occupation
        self.volunteer_interests = ', '.join(volunteer_interests)  # Convert list to string
        self.skills = ', '.join(skills)  # Convert list to string

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
