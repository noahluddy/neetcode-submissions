class PasswordManager:
    def __init__(self, pwd: str):
        self.__pwd = pwd
    
    # TODO: Implement the verify_password method
    def verify_password(self, pwd: str) -> bool:
        return pwd == self.__pwd



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
