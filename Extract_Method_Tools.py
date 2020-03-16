import nltk
nltk.download('punkt')

def methods_parse(directions):
    # parsing of the methods from the directions of a recipe

    all_methods = {  "Primary_cooking_method": [], "alternative_cooking_method": []  }
    PRIMARY_COOKING_METHODS = set([line.strip() for line in open('primaryCookingMethods.txt')])
    ALTERNATIVE_COOKING_METHODS = set([line.strip() for line in open('AlternativeCookingMethods.txt')])

    for raw_direction in directions:
        direction = nltk.word_tokenize(raw_direction)
        for dir in direction:
            if dir in PRIMARY_COOKING_METHODS:
                all_methods['Primary_cooking_method'].append(dir)
            if dir in ALTERNATIVE_COOKING_METHODS:
                all_methods['alternative_cooking_method'].append(dir)

        direction_bigrams = [direction[i:] for i in range(2)]
        direction_bigrams = zip(*direction_bigrams)
        direction_bigrams = [" ".join(d_bigram) for d_bigram in list(direction_bigrams)]

        for dir_bigram in direction_bigrams:
            if dir_bigram in PRIMARY_COOKING_METHODS:
                all_methods['Primary_cooking_method'].append(dir_bigram)
            if dir_bigram in ALTERNATIVE_COOKING_METHODS:
                all_methods['alternative_cooking_method'].append(dir_bigram)
    unique_primary_cooking_method= set(all_methods['Primary_cooking_method'])
    unique_alternative_cooking_method = set(all_methods['alternative_cooking_method'])
    all_methods['Primary_cooking_method'] = list(unique_primary_cooking_method)
    all_methods['alternative_cooking_method'] = list(unique_alternative_cooking_method)
    #print(all_methods)
    return all_methods

def tools_parse(directions):

    #parsing of the tools from the directions of a recipe
    list_of_tools = []
    TOOLS = set([line.strip() for line in open('tools.txt')])

    for raw_direction in directions:
        direction = nltk.word_tokenize(raw_direction)
        for dir in direction:
            if dir in TOOLS:
                list_of_tools.append(dir)

        tools_bigrams = [direction[i:] for i in range(2)]
        tools_bigrams = zip(*tools_bigrams)
        tools_bigrams = [" ".join(tool_bigram) for tool_bigram in list(tools_bigrams)]

        for tool_bigram in tools_bigrams:
            if tool_bigram in TOOLS:
                list_of_tools.append(tool_bigram)
    list_of_tools= list(set(list_of_tools))
    return list_of_tools


