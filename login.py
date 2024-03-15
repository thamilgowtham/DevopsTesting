def login():
    # Dictionary to store username-password pairs (replace with database in real application)
    user_credentials = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }

    # Get username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and the password matches
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful. Welcome, " + username + "!")
    else:
        print("Invalid username or password. Please try again.")

# Main function
if __name__ == "__main__":
    login()
