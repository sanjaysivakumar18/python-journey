print("🏝️ Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure.")
print("You wake up on a mysterious island after a shipwreck.")
print("In front of you, there is a dark forest and a dangerous river.")

choice1 = input('You see two paths. Do you go "left" into the forest or "right" towards the mountains? ').lower()

if choice1 == "left":
    print("\nYou enter the forest and walk for hours.")
    print("Suddenly, you find a river blocking your way.")

    choice2 = input('Do you "swim" across the river or "wait" for a boat? ').lower()

    if choice2 == "wait":
        print("\nYou wait patiently.")
        print("A mysterious old boat appears from the fog.")
        print("It takes you safely to the other side.")

        choice3 = input('You find three doors: "red", "blue", and "yellow". Which door do you choose? ').lower()

        if choice3 == "yellow":
            print("\n🎉 You open the yellow door...")
            print("Inside, you find a chest full of gold!")
            print("🏆 Congratulations! You found the treasure!")

        elif choice3 == "red":
            print("\n🔥 The red door opens into a room of fire.")
            print("Game Over!")

        elif choice3 == "blue":
            print("\n🌊 The blue door leads to a room filled with water.")
            print("Game Over!")

        else:
            print("\nYou choose a wrong door.")
            print("Game Over!")

    else:
        print("\nThe river is too dangerous.")
        print("You get swept away.")
        print("Game Over!")

else:
    print("\nYou walk towards the mountains.")
    print("A landslide blocks your path.")
    print("You cannot continue.")
    print("Game Over!")