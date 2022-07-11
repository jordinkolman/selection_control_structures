'''
Created on Monday Jul 11 13:16 2020

@author: Jordin Kolman
'''

temperature = float(input("What is the temperature: "))
condition = input("What are the cloud conditions? ") #assignment

if temperature > 70 and temperature < 90 and condition == 'sunny':
    print("It is nice outside:)")
elif temperature > 70 and temperature < 90 and condition != 'sunny':
    print("The temperature is nice. It's too bad the sun isn't out:(")
elif temperature < 70:
    print("It is too cold!")
else:
    print("It's way too hot out!")