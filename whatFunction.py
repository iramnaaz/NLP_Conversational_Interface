from PyDictionary import PyDictionary

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def removeNonLetter(ques):
    lettersOnly=[]
    for symbol in ques:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def whatIs(ques):
    NonLetterWords=removeNonLetter(ques)
    result= NonLetterWords.split(" ")
    #print(result[0])
    dictionary = PyDictionary()
    if result[0].lower().__contains__('what'):
        #print("yes")
        #print(result[2])

        meaning = dictionary.meaning(result[2])
        print(meaning)
    else:
        print("Question must Start with What dear..!")
    return result




def main():
    whatIs("What is oven?")

if __name__ == '__main__':
    main()


