print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

play_again = "yes"
while play_again.lower() == "yes":
    score = 0
    print("Okay, let's get started! :) ")

    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 'central processing unit'.")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 'graphics processing unit'.")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 'random access memory'.")

    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 'power supply unit'.")

    print("You have reached the end of the quiz!")
    print("You got " + str((score / 4) * 100) + "%.")

    play_again = input("Would you like to play again? (yes/no) ")

print("Thank you for playing! Goodbye!")