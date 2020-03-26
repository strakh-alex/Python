import random
import urllib.request

stages = [
"____________    ",
"|        |      ", 
"|        |      ", 
"|        0      ", 
"|       /|\     ", 
"|       / \     ", 
"|               "
]

def GetWord():
    print("Getting a random word...")
    word_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    return str(random.choice(words))

def GameOver(win):
    if(win == False):
        print("You loose!")
    else:
        print("You won!")

    while(True):
        print("Start a new game?")
        choise = input("Y/N: ")
        if(choise.lower() == 'y'):
            Hangman(GetWord())
        elif(choise.lower() == 'n'):
            print("Bye!")
            break

def NewGame():
    print("Hello! Let's start new game!")
    w = GetWord()
    print(w)
    Hangman(w)

def Hangman(word):
    wrong = 0
    round = 1
    keyword = []

    for item in word:
        keyword.append("_")

    while(wrong != len(stages)):
        status = stages[-(wrong+1):]
        for i in status:
            print(i)

        print(keyword)
        if("_" not in keyword):
            GameOver(True)

        letter = input("Enter a letter: ")

        if(letter.lower() in word.lower()):
            print("Correct!")
            print("")
            for i,item in enumerate(word):
                if(item == letter):
                    keyword[i] = letter
        else:
            print("Incorrect!")
            print("")
            wrong += 1

        round += 1

    GameOver(False)

NewGame()