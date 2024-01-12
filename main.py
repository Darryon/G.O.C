from Map import Map


def main():
    mymap = Map()
    for i in range(0, 29):
        for k in range(0,29):
            print(mymap.layout[i][k], end="")
        print("\n")


if __name__ == "__main__":
    main()