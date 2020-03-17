import enchant
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def removeNonLetter(ques):
    lettersOnly=[]
    for symbol in ques:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def whatIs(ques):
    output = "no result found"
    NonLetterWords=removeNonLetter(ques)
    result= NonLetterWords.split(" ")
    for i in result:
        isEnglish(i)
    if result[0].lower().__contains__('what'):
            syns = wordnet.synsets(result[len(result)-1])
            output = syns[0].definition()
    else:
        print("Question must Start with What dear..!")
    return output

def isEnglish(message):
    d = enchant.Dict("en_US")
    try:
      if d.check(message) == True:
         return
      else:
        print("Type only English Words dear!")
        exit()
    except ValueError:
        print("Don't write Numeric Value or please check if there is no extra space in Question...")
        exit()


def main():
    print(whatIs("WHAT IS AN OVEN?"))

if __name__ == '__main__':
    main()


