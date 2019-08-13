"""Template for json resumes

This module contains a class which can be invoked when creating a new resume,
as well as classes for creating resume elements
"""

def resume(dict):
    def __init__(self, location="": str, basics={}: dict, work=[]: list,
                 volunteer=[]: list, education=[]: list, awards=[]: list,
                 publications=[]: list, skills=[]: list, languages=[]: list,
                 interests=[]: list, references=[]: list):
        self.super().__init__(['basics': basics,
                               'work': work, 
			       'volunteer': volunteer,
                               'education': eductation, 
                               'awards': awards,
                               'publications': publications, 
                               'skills', skills,
                               'languages': languages, 
                               'interests': interests,
                               'references': references])
	self.location = location
