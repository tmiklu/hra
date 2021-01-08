import os
import random


print("Zahraj si hru kamen, papier a noznice")

print("Vzdy napise len jedno slovo: kamen, papier alebo noznice")

# score
your_score = 0

# game cycle
while True:
 
 if your_score == -1:
     print("Koniec hry, prehral si! ---> Tvoje score: " + str(your_score))
     break
 
 print("#########")
 print("Score: " + str(your_score), end='\n')
 print("#########")

 print("Tvoja volba:", end=' ')

 your_turn = input().lower()

 # computer
 computer_turn = [ "kamen", "papier", "noznice" ]
 computer_turn = random.choice(computer_turn)

 print("Super vybral: " + computer_turn)

 #main logic

 #kamen
 if "kamen" == your_turn or "papier" == your_turn or "noznice" == your_turn:
    if your_turn == "kamen":
        if your_turn == computer_turn:
            print("Remiza!")
        elif "kamen" != computer_turn:
            if "noznice" == computer_turn:
                print("-----> Vyhral si!")
                your_score += 1
            else:
                print("!!!--> Prehral si!")
                your_score -= 1
    
    # papier
    if your_turn == "papier":
        if your_turn == computer_turn:
            print("Remiza!")
        elif "papier" != computer_turn:
            if "kamen" == computer_turn:
                print("-----> Vyhral si!")
                your_score += 1
            else:
                print("!!!--> Prehral si!")
                your_score -= 1

    #noznice
    if your_turn == "noznice":
        if your_turn == computer_turn:
            print("Remiza!")
        elif "noznice" != computer_turn:
            if "papier" == computer_turn:
                print("-----> Vyhral si!")
                your_score += 1  
            else:
                print("!!!--> Prehral si!")
                your_score -= 1
 else:
     print("---->> !! Neplatna hodnota: " + str(your_turn))
