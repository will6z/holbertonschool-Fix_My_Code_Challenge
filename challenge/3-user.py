#!/usr/bin/python3
"""
User class
"""

class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email = None
        self.__password = None

    @property
    def email(self):
        """ Documentation """
        return self.__email

    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def password(self):
        """ Documentation """
        return self.__password

    @password.setter
    def password(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("password must be a string")
        self.__password = value

    def is_valid_password(self, pwd):
        """ Documentation """
        if pwd is None or type(pwd) is not str:
            return False
        return pwd == self.__password

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    u.password = "MyPassword"

    print(u.email)
    try:
        u.email = 42
    except Exception as e:
        print(e)
    
    print("is_valid_password should return True if it's the right password")
    if u.is_valid_password("MyPassword") is True:
        print("OK")
    else:
        print("is_valid_password should return True if it's the right password")

    print("is_valid_password should return False if it's not the right password")
    if u.is_valid_password("WrongPassword") is False:
        print("OK")
    else:
        print("is_valid_password should return False if it's not the right password")
