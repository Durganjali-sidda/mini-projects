import random

top_of_range = input("enter a Number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("enter a number larger tham 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()

random_num = random.randrange(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("enter a guess_Number: ")
    
    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
      print("please type a number next time.")
      continue
    
    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
            print("you are above the number")
    else:
            print("you are below the number")

print("You got it in", guesses,"guesses")
    