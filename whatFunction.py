from PyDictionary import PyDictionary


def whatIs(ques):
    result= ques.split(" ")
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


