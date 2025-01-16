import re
import sys
d

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

def main():
    #Check for a filename
    if len(sys.argv) < 2:
        print("Usage: python3 PartAHW1.py <file>")
        sys.exit(1)

    #Make text file path the first argument
    filepath = sys.argv[1]

    #Tokenize the file
    tokens = tokenize_file(filepath)

    #Get frequencies
    frequencies = token_frequency(tokens)

    #Print the frequencies in order
    for token, freq in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
        print(f"{token}: {freq}")

if __name__ == "__main__":
    main()