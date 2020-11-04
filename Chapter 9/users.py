#! python3

class User():
    """Represent a user profile."""

    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.email = email
        self.username = username
        self.hobby = hobby
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Password: {self.password}")
        print(f"  Username: {self.username}")
        print(f"  Hobby: {self.hobby}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        msg = f'Hello {self.first_name} {self.last_name}'
        print(msg)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempst(self):
        self.login_attempts = 0


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