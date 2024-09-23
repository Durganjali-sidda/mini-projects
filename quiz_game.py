print("Welcome to my Computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay let's play :) ")
score = 0

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("what does GUI stand for? ").lower()
if answer == "graphical user interface":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    


    
print("You got "+ str(score) + " questios correct!")
print("You got "+ str((score/4)*100) + "%.")