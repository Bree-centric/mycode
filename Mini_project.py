import random

def guess_favorite_hip_hop_song():
    songs = ["Juicy by The Notorious B.I.G.", "California Love by 2Pac", "Gin and Juice by Snoop Dogg", 
             "Empire State of Mind by Jay-Z", "Nuthin' But a 'G' Thang by Dr. Dre", "Shook Ones Part II by Mobb Deep",
             "C.R.E.A.M. by Wu-Tang Clan", "Changes by 2Pac", "Dear Mama by 2Pac", "Big Pimpin' by Jay-Z",
             "Mo Money Mo Problems by The Notorious B.I.G.", "It Was a Good Day by Ice Cube", "N.Y. State of Mind by Nas",
             "The Message by Grandmaster Flash & The Furious Five", "I Get Around by 2Pac", "Stan by Eminem",
             "Gangsta's Paradise by Coolio", "Regulate by Warren G", "Ms. Jackson by OutKast", "Ether by Nas",
             "99 Problems by Jay-Z", "Hypnotize by The Notorious B.I.G.", "The Next Episode by Dr. Dre",
             "In Da Club by 50 Cent", "Hit 'Em Up by 2Pac", "Keep Ya Head Up by 2Pac", "Still D.R.E. by Dr. Dre",
             "Lose Yourself by Eminem", "N.Y. State of Mind Part II by Nas", "Rapper's Delight by Sugarhill Gang",
             "Who Shot Ya by The Notorious B.I.G.", "Nuthin' But a 'G' Thang by Dr. Dre", "It's All About the Benjamins by Puff Daddy",
             "Ghetto Gospel by 2Pac", "Hard Knock Life (Ghetto Anthem) by Jay-Z", "The Real Slim Shady by Eminem",
             "Doo Wop (That Thing) by Lauryn Hill", "One Mic by Nas", "Warning by The Notorious B.I.G.",
             "The Rain (Supa Dupa Fly) by Missy Elliott", "Fight the Power by Public Enemy", "Scenario by A Tribe Called Quest"]
    return random.choice(songs)

def main():
    while True:
        print("\nWelcome to the Guess Your Favorite '90s Hip-Hop Song Quiz!")
        print("1. Guess Your Favorite '90s Hip-Hop Song")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Your favorite '90s Hip-Hop song:", guess_favorite_hip_hop_song())

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



