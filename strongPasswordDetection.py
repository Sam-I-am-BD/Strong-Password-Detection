#! python3
# Strong Password Detection
import re
# Prompt user to enter a new password
password = input('Please type your new password. ')
# Regexes to check for password strength and a list to pack the regex variables into a loop.
countRegex = re.compile(r'(.{8})')
lowerRegex = re.compile('[a-z]+')
upRegex = re.compile('[A-Z]+')
numRegex = re.compile('\d+')
rList = [countRegex, lowerRegex, upRegex, numRegex]
# Function to check the password for a character count, upper and lower case, and at least one number.
def passwdCheck(passwd):
    count = 0
    for i in rList:
        if i.search(passwd) == None:
                print('Error: Strong passwords should be at least 8 characters, have upper and lower case, and have at least one number.')
                break
        else:
            count += 1
    if count == 4:
        print('Congrats, this is a strong password!')
passwdCheck(password)
