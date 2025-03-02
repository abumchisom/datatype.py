'''Create a python script that collects user inputs and tells what data type it is.'''
# Importing the required libraries
#import sys

while True:
    userInput = input('Enter any value to check its data type:')
    
    try:
        userInput = eval(userInput)
    except:
        pass

    print(f'The data type of userInput is: {type(userInput)}')

    if type(userInput) == int:
        print('Your have entered an interger')

    elif type(userInput) == float:
        print('Your have entered a float')

    elif type(userInput) == str:
        print('Your have entered a string')

    elif type(userInput) == bool:
        print('Your have entered a boolean')

    elif type(userInput) == list:
        print('Your have entered a list')

    elif type(userInput) == tuple:
        print('Your have entered a tuple')

    elif type(userInput) == dict:
        print('Your have entered a dictionary')

    elif type(userInput) == set:
        print('Your have entered a set')

    elif type(userInput) == complex:
        print('Your have entered a complex number')

    elif type(userInput) == bytes:
        print('Your have entered a bytes')

    elif type(userInput) == bytearray:
        print('Your have entered a bytearray')  

    elif type(userInput) == memoryview:
        print('Your have entered a memoryview')

    else:
        print('Your have entered an invalid data type')
    #sys.exit()
    
    followup = input('Do you wish to continue? Y/N')
    if followup == 'Y' or followup == 'y':
        continue
   # elif followup != 'Y' or 'y':
    else:
        print('Thank you for using the program')
        break


