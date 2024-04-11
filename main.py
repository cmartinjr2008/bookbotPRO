def breakingBookApart(book):
     splitBook = book.split()
     return splitbook

def letterToLower(splitbook):
   for words in splitbook:
        if words.isalpha():
            for letter in words:
                lettersplit += letter.lower()

def letterCount(splitBook):
    letterCount = {}    
    #for x in range(len(splitBook)): add to lower if user choses for letter in words: lettersplit += letter.lower()
    for letter in splitBook:
        if letter in letterCount.keys():
            letterCount[letter] += 1
                    
        else:
            letterCount[letter] = 1
                              
    for letter in letterCount:
        print("The", letter, "character was found ", letterCount[letter], "times")

def wordCount(splitBook):
     numberOfWords = 0
     for words in splitBook:
        numberOfWords += 1
    
def killBookBot():
    print("Well be seeing ya!: ")
    exit()

def inputVerify(choice,filterType):
    verC = choice.lower()
    print(verC)
    print(choice)
    verified = False
    
    while verified == False:    
        if (filterType == "yesNoQuestion"):
            if verC == 'yes' or verC == 'n' or verC == 'no' or verC == 'quit':
                verified = True
            else:
                verified = False
        
        elif(filterType == "bookCase"):
            if verC == 'book' or verC == 'letters' or verC == 'both' or verC == 'quit':
                verified = True
            else:
                verified = False

        else:
            print("Sorry I didnt quite catch that, please try again!")
            verified = False
    return verC
    

with open('books/frankenstein copy.txt') as f:
    bookFile = f.read()
    splitbook = []
    lettersplit = []
     
    print("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _                                                ")
    print("       ! ! ! ! !     /  _    _   _____   _       _   ____   _   _  _   \\")
    print("       | O   O |    /  | |__| | |  _  | | |     | | |  _ \\ | |_| || |   \\")
    print("       |   v   | _ /   |  __  | | |_| |  \\ \\ ^ / /  | |_| | \\   / |_|   /")
    print("       | UUUUU |   \\   |_|  |_| |_____|   \\_/ \\_/   |____/   |_|  |_|  /")
    print("     __| nnnnn | __ \\_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _/")
    print(" - UUUU -------- UUUU --- ")
    print("| -------Munchin'------- |")
    print("| ----Uploaded Book------ |")
    print("| -----Hold Please . . .- |")
    print("| _______________________ |")
    print("                         ")
    print("                         ")
    splitbook = breakingBookApart(bookFile)

    print("Do you want to shift everything to lowercase?")
    verC = input("Type Yes or No: ")
    toLower = False
    verC = inputVerify(verC,"yesNoQuestion")
    if verC == 'yes':
        toLower = True
    else:
        toLower = False
    verC = None
    
    print("Great! Now do you want a report on letters, words or both?")
    verC = inputVerify()
    
       


    
   


    print(toLower)




        
        
         
    
   

    

    letterToLower(splitbook)
    


        


    

    print("There are a total of:", "words in this book")
    print("_________________________________")
    print("Here is the breakdown of letters: ")
    print("_________________________________")
    
    letterCount(lettersplit)