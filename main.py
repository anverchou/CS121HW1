import re

def tokenize_file(filepath):
    #Read the contents of the file
    with open(filepath, "r") as file:
        #Convert the text to lowercase
        text = file.read().lower()
    #Find all sequences of one or more alphanumeric characters
    tokens = re.findall(r"\w+", text)
    #Return the list of tokens
    return tokens

def token_frequency(tokens):
    #Set up map to for tokens
    token_count = {}
    for token in tokens:
        #If the token has already been counted
        if token in token_count:
            #Increment by 1
            token_count[token] += 1
        else:
            #Otherwise, set that token to one
            token_count[token] = 1
    #Return the count of the tokens
    return token_count

def token_list_count(tokens):
    return token

if __name__ == "__main__":
    filepath = "file.txt"
    tokens = tokenize_file(filepath)
    print(tokens)
    print(token_frequency(tokens))