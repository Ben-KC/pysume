"""Template for json resumes

This module contains a class which can be invoked when creating a new resume,
as well as classes for creating resume elements
"""

import collections
import datetime
import json


class Resume(collections.UserDict):
    def __init__(self, location: str="", basics: dict={}, work: list=[],
                 volunteer: list=[], education: list=[], awards: list=[],
                 publications: list=[], skills: list=[], languages: list=[],
                 interests: list=[], references: list=[]):
        super().__init__({'basics': basics,
                               'work': work, 
			       'volunteer': volunteer,
                               'education': education, 
                               'awards': awards,
                               'publications': publications, 
                               'skills': skills,
                               'languages': languages, 
                               'interests': interests,
                               'references': references})
        self.location = location

    categories = ["basics", "work", "volunteer", "education", "awards",
                  "publications", "skills", "languages", "interests",
                  "references"]
    
    def open_from_file(self, location: str):
        with open(location, 'r') as res:
            resume = json.load(res)

        for category in self.categories:
            self[category] = resume[category]

    def save(self):
        with open(self.location, 'w') as out:
            out.write(json.JSONEncoder().encode(self.data))

    def add_work(self, company: str, position: str, website: str,
                 summary: str, highlights: list, start_date: datetime.date, end_date: datetime.date=None):
        if end_date:
            end_date = end_date.isoformat()

        self["work"].append({"company": company,
                                      "position": position,
                                      "website": website,
                                      "startDate": start_date.isoformat(),
                                      "endDate": end_date,
                                      "summary": summary,
                                      "highlights": highlights})