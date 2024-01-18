from Map import Map
from Player import Player

#----------------------------------------------------------------
# Game Runner below
#----------------------------------------------------------------
Forest = Map()
def Start():
    temp = input("Hello travler, Please state your name.\n")
    character = Player(name=temp)
    print(f"Hello {character.getname()}, thats a nice name.")
    print(f"Well anyways {character.getname()}, there's no time to waste. Take this")
    input()
    print("*You drink a suspicious drink*\n")

    print("!You awake in a clearing. To the west is an abandoned house. All around you is forest.")
    print("!What shall you do first?")


def Walk(direction):
    Forest.move(direction)

def LookAround():
    #will return the left right top down objects in map based on player position
    print()



if __name__ == "__main__":
    Start()