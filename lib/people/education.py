from people import linkedin_base

class Education(linkedin_base.LinkedinBase):
    def __init__(self, education_linkedin):
        self.grade = education_linkedin.get('grade', '')
        self.degreeName = education_linkedin['degreeName']
        self.fieldOfStudy = education_linkedin['fieldOfStudy']
        self.schoolName = education_linkedin['schoolName']
        self.translate_date_range(education_linkedin['dateRange'])
        self.duration = self.get_duration()
        self.location = self.lookup_location(education_linkedin['schoolName'])

    def __repr__(self):
        return 'Education <{}, {}, {}, {} to {}>'.format(self.degreeName, self.fieldOfStudy, self.schoolName, self.start_date, self.end_date)

    def get_school_name(self):
        return self.schoolName

    def get_degree(self):
        return self.degreeName

    def get_major(self):
        return self.fieldOfStudy

    def get_grade(self):
        return self.grade
    
    def get_location(self):
        return self.location

    def predict_school_ranking(self):
        """ can start here:https://data.world/education/university-rankings-2017 """
        pass
    
