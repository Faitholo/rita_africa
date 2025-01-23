# Step 1: Initialize an empty dictionary to store users
user_database = {}

# Step 2: Function to register a user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = password
    print("Registration successful!")

# Step 3: Function to log in a user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")

# Step 4: Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# Step 5: View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Username: {username}")
    print("Welcome to your dashboard!")

# Step 6: Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = new_password
    print("Password updated successfully!")

# Step 7: Main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

# TASK 1: TODO
# Implement the dashboard so users can update their profile details
# The profile details should include Name, Address, Phone number & Date of Birth


# TASK 2: TODO
# Implement a task manager dashboard for registered users
# A user should be able to add tasks, view tasks, delete tasks and update tasks