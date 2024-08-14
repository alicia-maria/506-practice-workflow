# Import in the following packages into the Python file:
import pandas as pd
import numpy as np 

# Create the following variables and assign values 
number_variable = '100'
string_variable = "alicia"
Last_name_list = ['James', 'Williams', 'Stevenson', 'Harrison']

print(number_variable)  # '100'
print(string_variable)  # "alicia"
print(Last_name_list)  # ['James', 'Williams', 'Stevenson', 'Harrison']

# Python dictionary
Python_dictionary = [{
    'firstName': 'Michael',
    'lastName': 'Harrison',
    'age': 12, 
    'demographics': {
        'sex': 'male',
        'race': 'white'
    },
    'DOS': [8/12/24, 9/16/23, 7/18/22,],
    'address': {
        'street': '123 7th Street',
        'Zipcode': 1910,
        'city': 'East Northport'
    }
}]

print(Python_dictionary) 

# Function to categorize BMI
def bmi_categorization_tool(weight, height):
    """
    This Function categorizes BMI based on weight and height.

    Parameters Defined:
    Weight: In pounds 
    Height: In inches
    
    Returns:
    str: The BMI category.
    """
    # Calculate BMI
    bmi = (weight * 703) / (height ** 2)
    
    # Determine the BMI category
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi:
        return "Obesity"
    else:
        return "Invalid input"

# Example of tool performance
print(bmi_categorization_tool(250, 60))  # "Overweight"
print(bmi_categorization_tool(147, 65))  # "Normal weight"