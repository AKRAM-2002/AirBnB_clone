# test.py
import unittest

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def register_user(username, email):
    # Perform user registration logic, e.g., check for duplicate usernames or emails
    if username_exists(username) or email_exists(email):
        return None  # Registration failed
    else:
        new_user = User(username, email)
        # Save new user to the database or perform other necessary actions
        return new_user  # Registration successful

def username_exists(username):
    # Check if the username already exists in the system (simulated logic)
    existing_usernames = ["user1", "user2", "admin"]
    return username in existing_usernames

def email_exists(email):
    # Check if the email already exists in the system (simulated logic)
    existing_emails = ["user1@example.com", "user2@example.com", "admin@example.com"]
    return email in existing_emails

class TestUserManagement(unittest.TestCase):

    def test_register_user_success(self):
        # Test user registration with unique username and email
        new_user = register_user("newuser", "newuser@example.com")

        self.assertIsNotNone(new_user)  # Check that a user object is returned
        self.assertEqual(new_user.username, "newuser")
        self.assertEqual(new_user.email, "newuser@example.com")

    def test_register_user_username_exists(self):
        # Test user registration with an existing username
        new_user = register_user("user1", "newuser@example.com")

        self.assertIsNone(new_user)  # Check that registration fails

    def test_register_user_email_exists(self):
        # Test user registration with an existing email
        new_user = register_user("newuser", "user1@example.com")

        self.assertIsNone(new_user)  # Check that registration fails

if __name__ == '__main__':
    unittest.main()
