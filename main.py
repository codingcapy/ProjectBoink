
# Author: capybaraaa
# Date: March 25, 2022
# Version 1.00

class User:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

class Realtor:
    def __init__(self, f_name, l_name, region, rating):
        self.f_name = f_name
        self.l_name = l_name
        self.region = region
        self.rating = rating

class Rating:
    def __init__(self, grade, comment):
        self.grade = grade
        self.comment = comment

def main():
    pass

if __name__ == "__main__":
    main()