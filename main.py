import requests


def make_list():
    pass


def main():
    ready = input("Ready to begin? (Y/N) ")
    if ready and not ready.startswith("n") or ready == "":
        while True:
            print("What would you like to do? (1/2)")
            print("Option 1: Create list\nOption 2: Adjust priorities\nOption 3: Quit")
            option = input()
            if option == "1" or option.lower() == "option 1":
                print("Time to make a list!")
                make_list()
            elif option == "2" or option.lower() == "option 2":
                print("WIP")
            elif option == "3" or option.lower() == "option 3" or option.startswith("q"):
                print("See you later!")
                break
    else:
        print("Maybe another time!")


if __name__ == '__main__':
    main()
