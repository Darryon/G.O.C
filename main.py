from Map import Map
from Player import Player


def main():
    mymap = Map()
    
    for i in range(0, 29):
        for k in range(0,29):
            print(mymap.grid[i][k], end="")
        print("\n")


if __name__ == "__main__":
    main()