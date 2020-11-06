from random import * # importing random

user_pass = input("Enter your password: ") # taking input from user

# storing all possible chrecters
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','.',',','!','@','#','$','%','&',' ','(',')','-','_','+','=','*','^','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


guess = "" # initializing an empty string

# using while loop to generate many passwords untill one of
# them does not matches user_pass
count = 0
while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 78)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    count += 1
    print(guess,'-', count)
    
# printing the matched password
print("Your password is:",guess)
print('Total attempt taken:',count)