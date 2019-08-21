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
    
    # File I/O
    def open_from_file(self, location: str):
        with open(location, 'r') as res:
            resume = json.load(res)

        for category in self.categories:
            self[category] = resume[category]

    def save(self):
        with open(self.location, 'w') as out:
            out.write(json.JSONEncoder().encode(self.data))

    # Work section
    def add_work(self, company: str, position: str, website: str,
                 summary: str, highlights: list, start_date: datetime.date,
                 end_date: datetime.date=None):
        if end_date:
            end_date = end_date.isoformat()

        self["work"].append({"company": company,
                             "position": position,
                             "website": website,
                             "startDate": start_date.isoformat(),
                             "endDate": end_date,
                             "summary": summary,
                             "highlights": highlights})

    def remove_work(self, index: int):
        del self["work"][index]

    # Profile section    
    def add_profile(self, network: str, username: str, url: str):
        self["basics"]["profiles"].append({"network": network,
                                           "username": username,
                                           "url": url})

    def remove_profile(self, index: int):
        del self["basics"]["profiles"][index]

    def update_profile(self, index: int, network: str,
                       username: str, url: str):
        self["basics"]["profiles"][index].update({"network": network,
                                                  "username": username,
                                                  "url": url})

    # Volunteer section
    def add_volunteer(self, organization: str, position: str, website: str,
                      summary: str, highlights: list,
                      start_date: datetime.date, 
                      end_date: datetime.date=None):
        if end_date:
            end_date = end_date.isoformat()

        self["volunteer"].append({"organization": organization,
                                  "position": position,
                                  "website": website,
                                  "startDate": start_date.isoformat(),
                                  "endDate": end_date,
                                  "summary": summary,
                                  "highlights": highlights})

    def remove_volunteer(self, index: int):
        del self["volunteer"][index]

    # Education section
    def add_education(self, instution: str, area: str, study_type: str,
                      gpa: str, courses: list, start_date: datetime.date,
                      end_date: datetime.date=None):
        if end_date:
            end_date = end_date.isoformat()

        self["education"].append({"instution": instution,
                                  "area": area,
                                  "studyType": study_type,
                                  "gpa": gpa,
                                  "startDate": start_date.isoformat(),
                                  "endDate": end_date,
                                  "courses": courses})

    def remove_education(self, index: int):
        del self["education"][index]

    # Award section
    def add_award(self, title: str, date: str, awarder: str, summary: str):
        self["awards"].append({"title": title,
                               "date": date.isoformat(),
                               "awarder": awarder,
                               "summary": summary})

    def remove_award(self, index):
        del self["awards"][index]

    # Publication section
    def add_publication(self, name: str, publisher: str,
                        release_date: datetime.date, website: str,
                        summary: str):
        self["publications"].append({"name": name,
                                     "publisher": publisher,
                                     "releaseDate": release_date.isoformat(),
                                     "website": website,
                                     "summary": summary})

    def remove_publication(self, index):
        del self["publications"][index]

    # Skill section
    def add_skill(self, name: str, level: str, keywords: list):
        self["skills"].append({"name": name,
                               "level": level,
                               "keywords": keywords})

    def remove_skill(self, index):
        del self["skills"][index]

    # Language section
    def add_language(self, language: str, fluency: str):
        self["languages"].append({"language": language,
                                  "fluency": fluency})

    def remove_language(self, index):
        del self["languages"][index]

    # Interest section
    def add_interest(self, name: str, keywords: list):
        self["interests"].append({"name": name,
                                  "keywords": keywords})

    def remove_interest(self, index):
        del self["interests"][index]

    # Reference section
    def add_reference(self, name: str, reference: str):
        self["references"].append({"name": name,
                                   "reference": reference})

    def remove_reference(self, index):
        del self["references"][index]