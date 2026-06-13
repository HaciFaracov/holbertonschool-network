#!/usr/bin/python3
"""
User class module
"""
import hashlib

class User:
    """User class"""

    def __init__(self):
        """User constructor"""
        self.__email = None
        self.__password = None

    @property
    def email(self):
        """Getter for email"""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def password(self):
        """Getter for password"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """Setter for password"""
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """Validates password"""
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        # The bug was comparing the hash to 'pwd' instead of 'self.__password'
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password
