# In this assignment, you have to raise a custom exception and handle it.
# Ask the user to enter a password and once you read it, check the length of the password.
# If its length is < 8 characters long, raise an InvalidPasswordException, handle it using try-except,
# and display a user-friendly message to the users

class InvalidPasswordException(Exception):
    def __init__(self):
        self.message = "Insufficient password length"
    def __str__(self):
        return f"Error : {self.message} \n Re-enter password..."

if __name__ == "__main__":
    while True:
        try:
            passwd = input("Enter password : ")
            if len(passwd) < 8:
                raise InvalidPasswordException
            else: 
                print("Valid Password, proceed forward...")
                break
        except InvalidPasswordException as e:
            print(e)
    
