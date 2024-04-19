def welcomTxt():
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
    print("                           ")
    print("                           ")

def uploadTxtFile():
    with open('books/frankenstein copy.txt') as text:
        return text.read()

def letterToLower(lowerLetter):
    shiftedDoc = lowerLetter
    for i in range(0, len(shiftedDoc)):
            if (shiftedDoc[i].isalpha()):
                shiftedDoc[i] = shiftedDoc[i].lower()  
            
    return lowerLetter

#count how many characters are in each word of the txt file. 
def characterCount(splitBook):
    letterCount = {}
    wordExploder = []
    
    for word in splitBook: #loop through the string thats already been split
        for letter in word: #loop though each word and split
            if letter in letterCount.keys(): #Idefify if a ltter has a key postion if not add it to the list
                letterCount[letter] += 1 
            else:
                letterCount[letter] = 1

    for letter in letterCount:
        print(f"The {letter} character was found {letterCount[letter]} times")

#count how many words we have in the txt file
def wordCount(splitBook):  
    wordCount= {}
    numberOfWords = 0
    for words in splitBook:
        numberOfWords += 1
    
    for word in splitBook:
        if word in wordCount.keys():
            wordCount[word] += 1            
        else:
            wordCount[word] = 1
                              
    for word in wordCount:
        print(f"{word} was found a total of {wordCount[word]} times")

#Function to count and split letters.  
def comboCount(splitBook):
    letterCount = {}
    wordCount= {}    
    #for x in range(len(splitBook)): add to lower if user choses for letter in words: lettersplit += letter.lower()
    numberOfWords = 0
    for words in splitBook:
        numberOfWords += 1
    
    print(splitBook)
    for letter in splitBook:
        if letter in letterCount.keys():
            letterCount[letter] += 1
                    
        else:
            letterCount[letter] = 1

       
    numberOfWords = 0
    for words in splitBook:
        numberOfWords += 1
    
    for word in splitBook:
        if word in wordCount.keys():
            wordCount[word] += 1            
        else:
            wordCount[word] = 1
                              
    for word in wordCount:
        print(f"{word} was found a total of {wordCount[word]} times")

def killBookBot():
    print("Well be seeing ya!: ")
    exit()

def inputVerify(choice,filterType):
    verC = choice.lower()
    print(verC)
    verified = False
    
    while verified == False:    
        if (filterType == "yesNoQuestion"):
            if verC == 'yes' or verC == 'no' or verC == 'quit':
                verified = True 
            else:           
                print("Sorry I didnt quite catch that, please try again!")
                verC = None
                verified = False
                verC = input("Please enter Yes or No: ")
        
        elif(filterType == "bookCase"):
            if verC == 'words' or verC == 'letters' or verC == 'both' or verC == 'quit':
                verified = True
            else:
                print("Sorry I didnt quite catch that, please try again!")
                verified = False
                verC = input("Please enter Book, Letter, or Both: ")
    return verC

def main():
    txtDoc = []  
    welcomTxt()
    bookFile = uploadTxtFile()
    txtDoc = bookFile.split()
    print (txtDoc)

    print("Do you want to shift everything to lowercase?")
    verC = input("Type Yes or No: ")
    verC = inputVerify(verC,"yesNoQuestion")
    
    if(verC == "yes"):
        verC = None
        letterToLower(txtDoc)
                       
    else:
        verC = None

    print("\n")
    print("Great! Now do you want a report on letters, words or both?")
    verC = input("Enter Words, Letters, or Both: ")
    verC = inputVerify(verC, "bookCase")
    
    if(verC == "words"):
        wordCount(txtDoc)
   
    elif(verC == "letters"):
        characterCount(txtDoc)
   
    elif(verC == "both"):
        wordCount(txtDoc)
        characterCount(txtDoc)
       

if __name__ == "__main__":
    main()