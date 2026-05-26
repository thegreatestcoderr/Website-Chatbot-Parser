print("You wake up in a dark forest.")
choice = input("Do you go left or right? (left/right): ")

if choice == "left":
    print("You encounter a friendly dragon.")
    choice2 = input("Do you say 'Hi!' or 'Go away!'(make sure to copy exact phrases and capitalize start of words of phrases and make sure to include puntuation)")
    if choice2 == "Hi!":
        print("The dragon says hi back. Do you follow the dragon or leave?")
    elif choice2 == "Go away!":
        print("The dragon flies off, leaving you stranded. Do you follow the dragon or look for food?")
    else:
        print("Invalid choice. Please try again with correct capitilization and punctuation.")
elif choice == "right":
    print("You find a hidden treasure chest.")
    choice2 = input("Do you open the chest or go away and look for food?")
    if choice2 == "Open the chest.":
        print("You find weapons, armour, and an invitation to a palace. Do you follow the map on the invitation or go away and look for food?")
else:
    print("Invalid choice. Please try again with correct capitalization and punctuation.")