import random

lives=6
word_list=['Apple','Grape','Guava','Mango','Banana','potato']
chosen_word=random.choice(word_list)
print(chosen_word)
display_word=[]
for i in range(len(chosen_word)):
    display_word+='_'
print(display_word)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter :").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display_word[position]=guessed_letter
    print(display_word)         
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
             game_over=True
             print("you lose!")
    if '_' not in display_word:
        game_over=True
        print("you win!!")             
