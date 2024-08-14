# 506-practice-workflow
This assignment is as a primer for 504/507 Fall semester classes to practice a basic development workflow  


# intro_practice.py file contains the following information 
    #1. Basic import statements for pandas and numpy with short cuts 
    #2. Created basic integer variable 100 
        Created a string variable using my personal name 
        Created a basic list with string variables of patient last names 
       
        Created a python dictonary using demographic ; that has the following items 
    firstName': 'Michael',
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

    #3 Then I creates a BMI function that took 2 inputs which were as followed 
        Weight 
        Heigh 

        Then found basic calculation for BMI measurement and ranges and create the following formula and if else statements 

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

    After That all variables in the document contain print statement and example outputs 