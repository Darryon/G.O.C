
#used to copy and paste 
    #if playermove == "go north":
    #if playermove == "go east":
    #if playermove == "go south":
    #if playermove == "go west":

#Trying to figure out a way for the player to view their inventory at anytime during the game.
#     x=input()
# if x == "inventory":
#     print(inventory)
#     if "spellbook" in inventory:
#         print(spellbookSpells)
#     if "flute" in inventory:
#         print(fluteSpells)



#Game instructions



#imports
import random

#Area used to set Variables
Movement = ["go north", "go east", "go south"]
inventory = []
LostCharacter = 4
playerHP = 10
skillcheck = random.randint(1,20)
axeAttack = random.randint(5,15)

#magic
Fireball = random.randint(5,15)
Acid = random.randint(5,15)
Heal = playerHP + 5
Scream = random.randint(8,12)
spellbookSpells = ['Fireball', 'Acid' , 'Heal']
fluteSpells = ['Heal', 'Acid', 'Scream']
trollatk = random.randint(3,5)
#playerclass = none 
def Warrior():
    print("You are a mighty Warrior, use your awesome strength to defeat the Dragon in the dungeon")
    if 'axe' in inventory:
        playerHP + 30
def Wizard(): 
    print("You are an all powerful Wizard, use your powerful spellbook to cast fireball and defeat the Lich King in the dungeon")
    if 'spellbook' in inventory:
        playerHP + 10
def Bard():
    print("You are now a whimsical Bard, use your magical music to cast acid and defeat the Demon King in the dungeon")
    if 'flute' in inventory:
        playerHP + 20



#Game Start
   
Loop = 0.1
while True:  
    while Loop == 101:
        print("Do you wish to decend into the dungeon below.\nType 'yes' or 'no'.\n")
        yesorno = input()
        if yesorno == "yes":
            print("You decend into the dungeon.\n\nThank you for playing Episode 1 of GOC.\nStay tuned for Episode 2")
        if yesorno == "no":
            print("You try walking away from the steps but trip and fall forward down into the stairs.\nGame Over Coward!\n\nThank you for playing Episode 1 of GOC\nStay tuned for Episode 2")
    while Loop == 100:
        print("Do you wish to play again?")
        yesorno = input()
        if yesorno == "yes":
            Loop = 0
        if yesorno == "no":
            Loop = 0.5
    while Loop == 0.1:
        print("Welcome to Episode 1 of Game Over Coward aka GOC!!!\n\nInstructions:\n\nMovement: go north---go south---go east---go west\n\nGrab Item: Type the name of the item you want to grab\n\nAttack: Type 'hit [object] with [item]'\nExample: hit troll with axe\n\nHave fun and goodluck.\n")
        startGame = input("Type 'start' to play\n")
        
        if startGame == "start":
            print("\n\n\n\n\n")
            Loop = 1
        else:
            print("\nInvalid Input.")
            continue;
    




    while Loop == 0.5:
        print("Goodbye")
        print("\nRestart Game?")
        restartGame= input("yes or no\n")
        if restartGame == "yes":
            Loop = 0.1
        if restartGame == "no":
            exit()

    while Loop == 0:
        inventory = []
        Loop = 1




    while Loop == 1: 
        
        print("\nYou are in a clearing. To the west is an abandoned house. All around you is forest.")
        playermove = input()
        Movement = ["go north", "go east", "go south"]
        if playermove in Movement:
            LostCharacter = 4
            Loop = 1.1
            while Loop == 1.1:
                Movement = ["go east", "go south"]
                if playermove in Movement:
                    print("\nYou are in a forest")
                    LostCharacter = LostCharacter - 1
                    playermove = input()
                
                    if LostCharacter == 2 or LostCharacter == 1:
                    
                        print("\nYou are becoming lost.")
                    if LostCharacter == 0:
                        print("\nYou are lost and die due to starvation.\nGame Over Coward.")
                if playermove == "go north":
                    print("\nYou are in a forest. The trees around you close in but to the north you see a small dirt path")
                    playermove = input()
                    if playermove == "go west":
                        Loop = 1
                    if playermove in Movement:
                        if LostCharacter == 2 or LostCharacter == 1:
                    
                            print("\nYou are becoming lost.")
                        if LostCharacter == 0:
                            print("\nYou are lost and die due to starvation.\nGame Over Coward.")
                    if playermove == "go north":
                        Loop = 12
                        while Loop == 12:
                            print("\nYou are now on a small dirt path leading into a darker part of the forest. To the east you see a tree hollow with something tucked into it. To the north the path continues towards a cave.")
                            playermove = input()
                            if playermove == "go east":
                                if inventory == [] or inventory == ["bag of gold"] :
                                    print("\nYou walk over to the hollow. Inside you find a axe, a book, and a flute. You may only take one.\nChoose wisley.")   
                                    playerchoice = input()

                                if playerchoice == "axe":
                                    inventory.append("axe")
                                    playerclass = Warrior()
                                   
                                    print("The axe has been added to your inventory.")
                                
                                if playerchoice == "book":
                                    inventory.append("spellbook")
                                    playerclass = Wizard()
                                    
                                    print("The spellbook has been added to your inventory.")
                                
                                
                                if playerchoice == "flute":
                                    inventory.append("flute")
                                    playerclas = Bard()
                                    
                                    print("The magical flute has been added to your inventory.")
                                
                                if playermove == "go north" and 'axe' or 'spellbook' or 'flute' in inventory:
                                        print("The tree is now empty.")
                            if playermove == "go north":
                                print("\nYou are in a cave. A huge troll stands in your way. To the north of the troll is a door. To the south is the dirt path you came from.")
                                Loop = 13
                                trollHP = 30
                            while Loop == 13:
                                print("The troll looks angry.")
                                playermove = input()
                                
                                if playermove == "go south":
                                    Loop = 12
                                if playermove == "go north":
                                    if skillcheck >= 15:
                                        print("You jump through the troll's legs and dive through the door")
                                        Loop = 100
                                    if skillcheck < 15:
                                        print("\nYou try to dive through the troll's legs but the troll catches you. The troll proceedes to smash you into a bloody red paste.\nGame Over Coward.")
                                        Loop = 100
                                if playermove == "hit troll with axe" and "axe" in inventory and trollHP >= 0:
                                    
                                    
                                    trollHP = trollHP - axeAttack
                                    playerHP = playerHP - trollatk

                                
                                    if playerHP <=0:
                                        print("The troll has killed you.")
                                        Loop = 100
                                        break;

                                    Loop = 13
                                    if trollHP >= 0:
                                        print ("\nYou hit the troll with your axe")
                                        if trollHP <=10 and trollHP > 0:
                                            print("\nThe troll looks is covered in wounds and looks like its close to dying")
                                    
                                    if trollHP <= 0:
                                        print("\nThe troll falls dead to the ground")
                                        Loop = 100
                                    playermove = input()   
                                
                                    
                                if "spellbook" in inventory and playermove == "hit troll with fireball" and trollHP >= 0:
                                
                                    trollHP = trollHP - Fireball
                                    playerHP = playerHP - trollatk
                                    
                                    if playerHP <=0:
                                        print("The troll has killed you.")
                                        Loop = 100
                                        break;
                                    Loop = 13
                                    if trollHP >= 0:
                                        print("\nYou hit the troll with you fireball") 
                                        if trollHP <=10 and trollHP > 0:
                                            print("The troll looks is covered in wounds and looks like its close to dying")
                                    
                                    if trollHP <= 0:
                                        print("\nThe troll falls dead to the ground")
                                        Loop = 100
                                    playermove = input()

                                if "flute" in inventory and playermove == "hit troll with acid" and trollHP >= 0:
                                
                                    trollHP = trollHP - Acid
                                    playerHP = playerHP - trollatk
                                    
                                    if playerHP <=0:
                                        print("The troll has killed you.")
                                        Loop = 100
                                        break;
                                    Loop = 13
                                    if trollHP >= 0:
                                        print("\nYou hit the troll with acid")                                        
                                        if trollHP <=5 and trollHP > 0:
                                            print("\nThe troll looks is covered in wounds and looks like its close to dying")
                                    
                                    if trollHP <= 0:
                                        print("The troll falls dead to the ground")
                                        Loop = 100
                                    playermove = input()

                            


                if playermove == "go west":
                    break;
            
        
        elif playermove == "go west":
            Loop = 2
            
        


    LostCharacter = 5

    
    while Loop == 2:
        Movement = ["go north", "go east", "go south"]
        print("\nYou are now standing in front of a big white house. The door to the west is open.")
        playermove = input()
        if playermove in Movement:
            Loop = 1
        
        if playermove == "go west":
            Loop = 3

    LostCharacter = 5
    while Loop == 3:
        print("\nYou now stand inside the house. To the north there is a closet. To the south there is a fireplace. To the west there is a door slightly ajar. To the east is the door you came through.") 
        playermove = input()  
        if playermove == "go north":
            if inventory == [] or inventory == ["bag of gold"] :
                print("\nYou walk over to the cabinet and open it. Inside you find a axe, a book, and a flute. You may only take one.\nChoose wisley.")   
                playerchoice = input()

            if playerchoice == "axe":
                inventory.append("axe")
                playerclass = Warrior()
                
                print("The axe has been added to your inventory.")
            
            if playerchoice == "book":
                inventory.append("spellbook")
                playerclass = Wizard()
                
                print("The spellbook has been added to your inventory.")
            
            
            if playerchoice == "flute":
                inventory.append("flute")
                playerclas = Bard()
                
                print("The magical flute has been added to your inventory.")
            
            
            if playermove == "go north" and 'axe' or 'spellbook' or 'flute' in inventory:
                    print("The cabinet is now empty.")
                    
            continue;

        if playermove == "go south" and inventory != ["bag of gold"]:
            print("\nYou search the fireplace. After a couple of minutes you find a small hidden case tucked away inside the fireplace.\nYour hands are blackened with ash and dust. Inside the case you find a bag of gold.")
            inventory.append("bag of gold")
            print("The bag of gold has been added to your inventory")
        
            if "bag of gold" in inventory:
                print("\nThe fireplace is empty now.")
            continue;
        
        if playermove == "go west":
            Loop = 4
        
        if playermove == "go east":
            Loop = 2

    LostCharacter = 5
    while Loop == 4:   
        print("\nYou now stand in the kitchen of the house. To the west are kitchen cabinets. To the south is a moldy door covered in grime. To the north is a wall. To the east is the door you came through. ")
        playermove = input()
        if playermove == "go north":
            print("\nYou hit the wall face first")
            LostCharacter = LostCharacter - 1
            if LostCharacter == 1:
                print("\nYou have died due to stupidity.\nGame Over Coward.")
                
            continue;

        if playermove == "go east":
            Loop = 3
            
        if playermove == "go south":
            
            doorHP = 10
            while(doorHP >= 0):
                print("\nYou stand in front of the moldy door. It looks like it can be broken.")
                playerattack = input()
                if playerattack == "hit door with axe" and "axe" in inventory:
                    doorHP = doorHP - axeAttack
                    print ("You hit the door with your axe")
                    
                    
                if "spellbook" in inventory and playerattack == "hit door with fireball":
                    doorHP = doorHP - Fireball
                    print("You hit the door with you fireball")
                    
                if "flute" in inventory and playerattack == "hit door with acid":
                    doorHP = doorHP - Acid
                    print("You hit the door with acid")
                if doorHP <=5 and doorHP > 0:
                    print("The door looks like its about to break")
                    
                if doorHP <= 0:
                    print("The door cracks and crumbles to dust leaving an open hole in the wall. You see stairs leading down.")
                    Loop = 101
                    
                                
        if playermove == "go west":
            if "health potion" not in inventory:
                print("After searching all the cabinets you are able to find a health potion.")
            inventory.append("health potion")
            if "health potion" in inventory:
                print("The cabinets are now empty")
            continue;
        
