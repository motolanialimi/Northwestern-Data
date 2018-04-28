# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "r" ): print("it's a tie")

elif( user_choice == "p" and computer_choice =="r"): print("(Paper Wins")

elif( user_choice == "s" and computer_choice == "r" ): print("Rock Wins")    
    
elif( user_choice =="p" and computer_choice == "s") : print("Scissors Wins")

elif( user_choice =="p" and computer_choice == "p" ): print("Sorry it's a tie")     