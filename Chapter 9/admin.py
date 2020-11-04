#! python3

from user import User

class Admin(User):
    """Represent a Admin user"""
    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        super().__init__(first_name, last_name, password, email, username, hobby, location)
        self.privileges = Priviliges()


class Priviliges():

    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"* {privilege}")
        else:
            print("- This user has no privileges.")