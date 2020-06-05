# City of Python

class Citizen:
    """This person is now a member of the City of Python"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
    greeting = "For the glory of Python!"
