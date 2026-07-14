import random
word_list=["apple","banana","orange","school","computer"]
chosen_word=random.choice(word_list)
display=[]
for letter in chosen_word:
    display.append("_")
lives=6
while lives>0:
    print("\nCurrent Word:")
    print(" ".join(display))
    guess=input("Guess a letter: ").lower()
    correct_guess=False
    
    for position in range(len(chosen_word)):
        if chosen_word[position]==guess:
            display[position]=guess
            correct_guess=True
    if not correct_guess:
        lives-=1
        print("Wrong Guess!")
        print("Lives Left:",lives)
    else:
        print("Correct guess")
    if "_" not in display:
        print("\You Win")
        print("The word was:",chosen_word)
        break
if lives==0:
    print("You Lose!")
    print("The word was:",chosen_word)
    
    
    