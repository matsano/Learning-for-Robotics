import numpy as np

class User:
    def __init__(self):
        self.dtype = [('name', 'U50'), ('age', int), ('height', float), ('weight', float), ('BMI', float), ('category', 'U50'), ('goal', 'U50')]
    
    def get_name(self):
        # Enter name
        name = input('Enter name: ')
        # while database.get_user(name) != None:
        #     name = input('This name already exists. Enter a new name: ')
            
        return name
    
    
    def get_age(self):
        # Enter age
        valid_age = False
        while not valid_age:
            try:
                age = int(input('Enter age: '))
                valid_age = True
            except:
                print("Error: not a valid age")
        return age
    
    
    def get_height(self):
        # Enter height
        valid_height = False
        while not valid_height:
            try:
                height = float(input('Enter height (in meters): '))
                valid_height = True
            except:
                print("Error: not a valid height")
        
        return height
    
    
    def get_weight(self):
        # Enter weight
        valid_weight = False
        while not valid_weight:
            try:
                weight = float(input('Enter weight (in kg): '))
                valid_weight = True
            except:
                print("Error: not a valid weight")
                
        return weight
    
    
    def calculate_BMI(self, height, weight):
        # Calculate Body Mass Index (BMI)
        return weight / (height**2)
    
    def get_category_BMI(self, BMI):
        # Get the category according to BMI
        if BMI < 16:
            return 'Underweight (Severe thinness)'
        elif BMI >= 16 and BMI < 17:
            return 'Underweight (Moderate thinness)'
        elif BMI >= 17 and BMI < 18.5:
            return 'Underweight (Mild thinness)'
        elif BMI >= 18.5 and BMI < 25:
            return 'Normal range'
        elif BMI >= 25 and BMI < 30:
            return 'Overweight (Pre-obese)'
        elif BMI >= 30 and BMI < 35:
            return 'Obese (Class I)'
        elif BMI >= 35 and BMI < 40:
            return 'Obese (Class II)'
        else:
            return 'Obese (Class III)'
    
    
    def get_user_goal(self):
        # Enter the goal of the user
        weight_loss = 'Weight loss'
        muscle_gain = 'Muscle gain'
        physical_end = 'Physical endurance'
        print("\Goals:")
        print("1.", weight_loss)
        print("2.", muscle_gain)
        print("3.", physical_end)

        option = input("Choose an option: ")

        if option == '1':
            return weight_loss
        elif option == '2':
            return muscle_gain
        elif option == '3':
            return physical_end
        
        
    def get_new_user(self):
        # Get informations from the user
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        weight = self.get_weight()
        BMI = self.calculate_BMI(height, weight)
        category = self.get_category_BMI(BMI)
        goal = self.get_user_goal()
        
        # Return the informations of the new user
        return np.array([(name, age, height, weight, BMI, category, goal)], dtype=self.dtype)