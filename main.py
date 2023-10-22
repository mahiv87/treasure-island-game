print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure!")

left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if left_or_right.lower() == "right":
    print("You fell into a pit of venomous lobsters! Game over.")
if left_or_right.lower() == "left":
    swim_wait = input("You arrive at a river. Do you want to swim or wait for a boat? Type 'swim' or 'wait'\n")
    if swim_wait.lower() == "swim":
        print("Your leg became trapped in a beaver's dam and you drowned! Game over.")
    if swim_wait.lower() == 'wait':
        door = input("You arrive at three mystery doors. Choose 'red', 'blue', or 'yellow'\n")
        if door.lower() == 'red' or door.lower() == 'blue':
            print("The door locks behind you. No one hears from you again... Game over.")
        elif door.lower() == "yellow":
            print("Congratulations you found the treasure!")
        else:
            print("The Gods have smite you! Game over.")
    else:
        print("The Gods have smite you! Game over.")
else:
    print("The Gods have smite you! Game over.")