import numpy as np
from newUser import newUser

class DataBase:
    def __init__(self):
        # Initialize the database as an empty array with a custom dtype
        self.dtype = [('name', 'U50'), ('age', int), ('height', float), ('weight', float), ('BMI', float), ('category', 'U50')]
        self.data = np.array([], dtype=self.dtype)


    def add_new_user(self):
        # Add a new user to the database
        user = newUser()
        new_user = user.get_new_user()
        self.data = np.append(self.data, new_user)
        
        return 0
    
    
    def print_informations(self, user):
        print(f'Name: {user["name"]}, Age: {user["age"]}, Height: {user["height"]}, Weight: {user["weight"]}, BMI: {user["BMI"]:.2f}, Category: {user["category"]}')
        
        return 0


    def get_all_users(self):
        # Returns all records in the database
        for user in self.data:
                self.print_informations(user)
        
        return 0


    def get_user(self):
        # Get the name of the user
        name = input('Enter the name to search: ')
        
        # Searches for an user by name and returns the first match found
        user_found = self.data[self.data["name"] == name]
        if user_found.size > 0:
            user = user_found[0]
            self.print_informations(user)
        else:
            print('User not found.')
        
        return 0

