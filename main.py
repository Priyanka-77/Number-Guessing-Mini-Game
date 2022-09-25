import random
import site
top_of_range = int(input("Type a number: "))
if top_of_range <= 0:
        print("Please type a number greater than zero next time")
    
        
else:        
    print("Please type a number next time")

    
random_number = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        #if user_guess <= 0:                                         #you can also do this or not
            #print("Please type a number greater than 0 next time")
            #quit()
    else:
        print("Please type a number next time")
        continue
        
    if user_guess == random_number:
        print("You got it correct!")
        break
    elif user_guess > random_number:
            print("You were above the number")
    else:
        print("You were below the number")
            
print("You got in", guesses, "guesses")            
            
    
