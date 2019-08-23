"""Template for json resumes

This is a module containing a class for opening and manipulating a json resume
in python.

Classes:
---
Resume: extends UserDict and provides methods for creating and managing the
        resume object
"""

import collections
import datetime
import json


class Resume(collections.UserDict):
    """Represents a json resume in python and provides methods for management

    This class extends functionality of UserDict. UserDict's __init__ is called 
    and used to set the initial value of the data variable. Additional methods 
    are provided which allow for easier manipulation of the resume's contents.

    Methods:
    ---
    add_award
    add_education
    add_interest
    add_language
    add_profile
    add_publication
    add_reference
    add_skill
    add_volunteer
    add_work
    open_from_file
    remove_award
    remove_education
    remove_interest
    remove_language
    remove_profile
    remove_publication
    remove_reference
    remove_skill
    remove_volunteer
    remove_work
    save
    update_award
    update_education
    update_interest
    update_language
    update_profile
    update_publication
    update_reference
    update_skill
    update_volunteer
    update_work

    Variables:
    ---
    categories - list of top-level categories in a json resume
    data - dict inherited from UserDict
    location - string containing the url to open from/save to
    """

    def __init__(self, location: str="", basics: dict={}, work: list=[],
                 volunteer: list=[], education: list=[], awards: list=[],
                 publications: list=[], skills: list=[], languages: list=[],
                 interests: list=[], references: list=[]) -> None:
        """Constructor for the Resume class

        Calls UserDict's __init__ to set the values of the data attribute and 
        sets the location variable. The data stored represents the contents of
        a json resume.

        Return: None

        Arguments:
        ---
        location - optional string containing the url to open from/save to
        basics - optional dict containing basic information
        work - optional list containing a dict for each place worked
        volunteer - optional list containing a dict for each act of volunteerism
        education - optional list containing a dict for each school attended
        awards - optional list containing a dict for each award received
        publications - optional list containing a dict for each published work
        skills - optional list containing a dict for each skill
        languages - optional list containing a dict for each language
        interests - optional list containing a dict for each interest
        references - optional list containing a dict for each reference
        """

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
    def open_from_file(self, location: str) -> None:
        """Fills in the Resume instance using the specified json resume

        Returns: None

        Arguments:
        ---
        location - string containing the url from which to open
        """

        with open(location, 'r') as res:
            resume = json.load(res)

        self.data.update(resume)

        self.location = location

    def save(self) -> None:
        """Writes the Resume instance to a json file

        Returns: None
        Arguments: None
        """

        with open(self.location, 'w') as out:
            out.write(json.JSONEncoder().encode(self.data))


    # Basics section
    def update_basics(self, name: str, label: str, picture: str, email: str,
                      phone: str, website: str, summary: str) -> None:
        """Updates the basic information

        Updates all of the resume's basic information, with the exception of 
        location and social media profiles

        Returns: None

        Arguments:
        ---
        name - string containing the applicant's name
        label - string containing the applicant's title
        picture string containing the location of the applicant's photo
        email - string containing the applicant's email address
        phone - string containing the applicant's phone number
        website - string containing the url of the applicant's website
        summary - string containing a description of the applicant
        """

        self["basics"].update({"name": name,
                               "label": label,
                               "picture": picture,
                               "email": email,
                               "phone": phone,
                               "website": website,
                               "summary": summary})

    def update_location(self, address: str, postal_code: str, city: str,
                        country_code: str, region: str) -> None:
        """Updates the location information

        Returns: None

        Arguments:
        ---
        address - string containing the street address
        postal_code - string containing the postal/zip code
        city - string containing the city name
        country_code - string containing the country code (ex: 'US')
        region - string containing the name of the region or state
        """

        self["basics"]["location"].update({"address": address,
                                           "postalCode": postal_code,
                                           "city": city,
                                           "countryCode": country_code,
                                           "region": region})

    def add_profile(self, network: str, username: str, url: str) -> None:
        """Adds a new entry to the profile list
        
        Returns: None

        Arguments:
        ---
        network - string containing the name of the social network
        username - string containing the username
        url - string containing the network's url
        """

        self["basics"]["profiles"].append({"network": network,
                                           "username": username,
                                           "url": url})

    def remove_profile(self, index: int) -> None:
        """Removes the specified profile entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which profile entry is to be removed
        """

        del self["basics"]["profiles"][index]

    def update_profile(self, index: int, network: str,
                       username: str, url: str) -> None:
        """Updates the specified profile entry
        
        Returns: None

        Arguments:
        ---
        index - integer indicating which profile entry is to be updated
        network - string containing the name of the social network
        username - string containing the username
        url - string containing the network's url
        """
        self["basics"]["profiles"][index].update({"network": network,
                                                  "username": username,
                                                  "url": url})


    # Work section
    def add_work(self, company: str, position: str, website: str,
                 summary: str, highlights: list, start_date: datetime.date,
                 end_date: datetime.date=None) -> None:
        """Adds a new entry to the work list

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        company - string containing the name of the company worked for
        position - string containing the title of the position worked
        website - string containing the url of the company's website
        summary - string containing a summary of the position
        highlights - list containing highlighted points from the position
        start_date - date that the position began
        end_date - optional date that the position ended
        """
        if end_date:
            end_date = end_date.isoformat()

        self["work"].append({"company": company,
                             "position": position,
                             "website": website,
                             "startDate": start_date.isoformat(),
                             "endDate": end_date,
                             "summary": summary,
                             "highlights": highlights})

    def remove_work(self, index: int) -> None:
        """Removes the specified work entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which work entry is to be removed
        """

        del self["work"][index]

    def update_work(self, index: int, company: str, position: str,
                    website: str, summary: str, highlights: list,
                    start_date: datetime.date, end_date: datetime.date=None) -> None:
        """Updates the specified work entry

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        index - integer indicating which work entry is to be updated
        company - string containing the name of the company worked for
        position - string containing the title of the position worked
        website - string containing the url of the company's website
        summary - string containing a summary of the position
        highlights - list containing highlighted points from the position
        start_date - date that the position began
        end_date - optional date that the position ended
        """

        if end_date:
            end_date = end_date.isoformat()

        self["work"][index].update({"company": company,
                                    "position": position,
                                    "website": website,
                                    "startDate": start_date.isoformat(),
                                    "endDate": end_date,
                                    "summary": summary,
                                    "highlights": highlights})


    # Volunteer section
    def add_volunteer(self, organization: str, position: str, website: str,
                      summary: str, highlights: list,
                      start_date: datetime.date, 
                      end_date: datetime.date=None) -> None:
        """Adds a new entry to the volunteer list

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        organization - string containing the name of the organization
        position - string containing the name of the volunteer position
        website - string containing the url of the organization
        summary - string containing a summary of the volunteer work
        highlights - list containing highlighted points from the position
        start_date - date the volunteer work began
        end_date - optional date the volunteer work ended
        """

        if end_date:
            end_date = end_date.isoformat()

        self["volunteer"].append({"organization": organization,
                                  "position": position,
                                  "website": website,
                                  "startDate": start_date.isoformat(),
                                  "endDate": end_date,
                                  "summary": summary,
                                  "highlights": highlights})

    def remove_volunteer(self, index: int) -> None:
        """Removes the specified volunteer entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which volunteer entry is to be removed
        """

        del self["volunteer"][index]

    def update_volunteer(self, index: int, organization: str, position: str,
                         website: str, summary: str, highlights: list,
                         start_date: datetime.date,
                         end_date: datetime.date=None) -> None:
        """Updates the specified volunteer entry

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        index - integer indicating which volunteer entry is to be updated
        organization - string containing the name of the organization
        position - string containing the name of the volunteer position
        website - string containing the url of the organization
        summary - string containing a summary of the volunteer work
        highlights - list containing highlighted points from the position
        start_date - date the volunteer work began
        end_date - optional date the volunteer work ended
        """

        if end_date:
            end_date = end_date.isoformat()

        self["volunteer"][index].update({"organization": organization,
                                         "position": position,
                                         "website": website,
                                         "startDate": start_date.isoformat(),
                                         "endDate": end_date,
                                         "summary": summary,
                                         "highlights": highlights})


    # Education section
    def add_education(self, institution: str, area: str, study_type: str,
                      gpa: str, courses: list, start_date: datetime.date,
                      end_date: datetime.date=None) -> None:
        """Adds a new entry to the education list

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        institution - string containing the name of the institution attended
        area - string containing the area studied
        study_type - string containing the level at which the area was studied
        gpa - string containing the current or graduating gpa
        courses - list containing relevant courses taken
        start_date - date the education began
        end_date - optional date the education was completed
        """

        if end_date:
            end_date = end_date.isoformat()

        self["education"].append({"institution": institution,
                                  "area": area,
                                  "studyType": study_type,
                                  "gpa": gpa,
                                  "startDate": start_date.isoformat(),
                                  "endDate": end_date,
                                  "courses": courses})

    def remove_education(self, index: int) -> None:
        """Removes the specified education entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which education entry is to be removed
        """
        del self["education"][index]

    def update_education(self, index: int, institution: str, area: str,
                         study_type: str, gpa: str, courses: list,
                         start_date: datetime.date,
                         end_date: datetime.date=None) -> None:
        """Update the specified education entry

        Note about the dates: dates are converted to isoformat strings before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        index - integer indicating which education entry is to be removed
        institution - string containing the name of the institution attended
        area - string containing the area studied
        study_type - string containing the level at which the area was studied
        gpa - string containing the current or graduating gpa
        courses - list containing relevant courses taken
        start_date - date the education began
        end_date - optional date the education was completed
        """

        if end_date:
            end_date = end_date.isoformat()

        self["education"][index].update({"institution": institution,
                                         "area": area,
                                         "studyType": study_type,
                                         "gpa": gpa,
                                         "startDate": start_date.isoformat(),
                                         "endDate": end_date,
                                         "courses": courses})


    # Award section
    def add_award(self, title: str, date: datetime.date, awarder: str,
                  summary: str) -> None:
        """Adds a new entry to the awards list
        
        Note about the date: the date is converted to an isoformat string before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        title - string containing the title of the award
        date - date the award was received
        awarder - string containing the giver of the award
        summary - string containing a description of the award
        """

        self["awards"].append({"title": title,
                               "date": date.isoformat(),
                               "awarder": awarder,
                               "summary": summary})

    def remove_award(self, index: int) -> None:
        """Removes the specified award entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which award entry is to be removed
        """

        del self["awards"][index]

    def update_award(self, index: int, title: str, date: datetime.date, awarder: str,
                     summary: str) -> None:
        """Updates the specified award entry
        
        Note about the date: the date is converted to an isoformat string before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        index - integer indicating which award entry is to be updated
        title - string containing the title of the award
        date - date the award was received
        awarder - string containing the giver of the award
        summary - string containing a description of the award
        """

        self["awards"][index].update({"title": title,
                                      "date": date.isoformat(),
                                      "awarder": awarder,
                                      "summary": summary})


    # Publication section
    def add_publication(self, name: str, publisher: str,
                        release_date: datetime.date, website: str,
                        summary: str) -> None:
        """Adds a new entry to the publications list

        Note about the date: the date is converted to an isoformat string before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        name - string containing the name of the published work
        publisher - string containing the name of the publisher
        release_date - date the publication was released
        website - string containing the url for the publication's website
        summary - string containing a description of the published work
        """

        self["publications"].append({"name": name,
                                     "publisher": publisher,
                                     "releaseDate": release_date.isoformat(),
                                     "website": website,
                                     "summary": summary})

    def remove_publication(self, index: int) -> None:
        """Removes the specified publication entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which publication entry is to be removed
        """
        del self["publications"][index]

    def update_publication(self, index: int, name: str, publisher: str,
                        release_date: datetime.date, website: str,
                        summary: str) -> None:
        """Updates the specified publication entry

        Note about the date: the date is converted to an isoformat string before
        being stored. This is done because JSONEncoder does not support
        encoding the datetime type.

        Returns: None

        Arguments:
        ---
        index - integer indicating which publication entry is to be updated
        name - string containing the name of the published work
        publisher - string containing the name of the publisher
        release_date - date the publication was released
        website - string containing the url for the publication's website
        summary - string containing a description of the published work
        """
        self["publications"][index].update({"name": name,
                                            "publisher": publisher,
                                            "releaseDate": release_date.isoformat(),
                                            "website": website,
                                            "summary": summary})


    # Skill section
    def add_skill(self, name: str, level: str, keywords: list) -> None:
        """Adds a new entry to the skills list

        Returns: None

        Arguments:
        ---
        name - string containing the name of the skill
        level - string containing the level of proficiency in the skill
        keywords - list containing keywords relating to the skill
        """

        self["skills"].append({"name": name,
                               "level": level,
                               "keywords": keywords})

    def remove_skill(self, index: int) -> None:
        """Removes the specified skill entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which skill entry is to be removed
        """

        del self["skills"][index]

    def update_skill(self, index: int, name: str, level: str,
                     keywords: list) -> None:
        """Updates the specified skill entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which skill entry is to be updated
        name - string containing the name of the skill
        level - string containing the level of proficiency in the skill
        keywords - list containing keywords relating to the skill
        """

        self["skills"][index].update({"name": name,
                               "level": level,
                               "keywords": keywords})


    # Language section
    def add_language(self, language: str, fluency: str) -> None:
        """Adds a new entry to the languages list

        Returns: None

        Arguments:
        ---
        language - string containing the name of the language
        fluency - string containing the level of fluency in the language
        """

        self["languages"].append({"language": language,
                                  "fluency": fluency})

    def remove_language(self, index: int) -> None:
        """Removes the specified language entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which language entry is to be removed
        """
        del self["languages"][index]

    def update_language(self, index: int, language: str,
                        fluency: str) -> None:
        """Updates the specified language entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which language entry is to be updated
        language - string containing the name of the language
        fluency - string containing the level of fluency in the language
        """

        self["languages"][index].update({"language": language,
                                         "fluency": fluency})


    # Interest section
    def add_interest(self, name: str, keywords: list) -> None:
        """Adds a new entry to the interests list

        Returns: None

        Arguments:
        ---
        name - string containing the name of the interest
        keywords - list containing keywords relating to the interest
        """

        self["interests"].append({"name": name,
                                  "keywords": keywords})

    def remove_interest(self, index: int) -> None:
        """Removes the specified interest entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which interest entry is to be removed
        """

        del self["interests"][index]

    def update_interest(self, index: int, name: str, keywords: list) -> None:
        """Updates the specified interest entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which interest entry is to be updated
        name - string containing the name of the interest
        keywords - list containing keywords relating to the interest
        """

        self["interests"][index].update({"name": name,
                                         "keywords": keywords})


    # Reference section
    def add_reference(self, name: str, reference: str) -> None:
        """Adds a new entry to the reference list

        Returns: None

        Arguments:
        ---
        name - string containing the name of the reference
        reference - string containing a statement from the reference
        """

        self["references"].append({"name": name,
                                   "reference": reference})

    def remove_reference(self, index: int) -> None:
        """Removes the specified reference entry

        Returns: None

        Arguments:
        ---
        index - integer indicating which reference entry is to be removed
        """

        del self["references"][index]

    def update_reference(self, index: int, name: str, reference: str) -> None:
        """Adds a new entry to the reference list

        Returns: None

        Arguments:
        ---
        index - integer indicating which reference entry is to be updated
        name - string containing the name of the reference
        reference - string containing a statement from the reference
        """

        self["references"][index].update({"name": name,
                                          "reference": reference})