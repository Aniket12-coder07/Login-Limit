class LoginSystem:
    def __init__(self, max_attempts=3):
        self.username = "Hello"  # Example username
        self.password = "World"  # Example password
        self.max_attempts = max_attempts
        self.attempts = 0

    def login(self):
        while self.attempts < self.max_attempts:
            user_input = input("Enter username: ")
            pass_input = input("Enter password: ")

            if user_input == self.username and pass_input == self.password:
                print("Login successful!")
                return True
            else:
                self.attempts += 1
                print(f"Login failed! You have {self.max_attempts - self.attempts} attempts left.")

        print("Too many failed attempts! You are locked out.")
        return False

if __name__ == "__main__":
    login_system = LoginSystem()
    login_system.login()