import random# import random module
print('Choose a Number Between 1 to 10')
lives = 5 # set a variable to give a 5 lives
while 0 < lives: # true until it reach 5 count
    try: # set a try except to handle error and continue the program
        print(f'You Have {lives} Lives')# update to the lives
        r = random.randint(1,10) # creat random numbers from 1 to 10
        userinput = int(input('Enter Your Number : \n')) # ask a user to what number input 
        if lives == 1 : #once lives is equal to 1 it print gameover
            print('GameOver')
        elif lives > 0: #once lives is graeter than to 0 it bring down 
            if userinput == r : # check if true userinput is equal to the random number it print the the code below
                print('Congratulation !!! You guess The correct number..')
                break # break the loop
            else:# once if statement become false it print the code below
                print('Please Try Again..')
    except ValueError:# handle the valueerror
         print('Digit Only')
         lives+=1   # increment the lives   
    lives -= 1 # decrement the lives