import requests


def make_search(search):
    url = f"https://api.deezer.com/search?q={search}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["data"]
        print("We found results:")
        print(data)
    else:
        print("An error has occurred accessing the API.")


def make_list():
    creating = True
    while creating:
        search = input("Write the title of a song to search for it, or \"q\" to quit: ")
        if creating == "q":
            creating = False
        else:
            make_search(search)


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
                # Genre, Similar Artist, Same Artist, Release Date, Band / Solo Artist, Instrumentation, Mood / Vibe
            elif option == "3" or option.lower() == "option 3" or option.startswith("q"):
                print("See you later!")
                break
    else:
        print("Maybe another time!")


if __name__ == '__main__':
    main()
