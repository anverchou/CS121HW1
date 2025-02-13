import re
import sys
from collections import defaultdict

#Time Complexity: O(N)
#Open and reads the size of the file
#Reads every character to convert text to lowercase
#Scans input once in re.findall
#Tokenize text file
def tokenize_file(filepath):
    try:
        #Open file
        with open(filepath, "r") as file:
            #Convert the text to lowercase
            text = file.read().lower()
        #Tokenize alphanumeric characters
        tokens = re.findall(r"[a-z0-9]+", text)
    #Error handling for filepath
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)
    #Error handling for file reading
    except IOError:
        print(f"Error reading file: {filepath}")
        sys.exit(1)
    #Return the list of tokens
    return tokens

#Time Complexity: O(N)
#Loop through the list of tokens
#Loockups are O(1), however, because of the n number of tokens, this becomes O(n)
#Function to count the number of tokens
def token_frequency(tokens):
    #Map for tokens
    token_count = {}
    for token in tokens:
        try:
            #If the token has already been counted
            if token in token_count:
                #Increment that token by one
                token_count[token] += 1
            else:
                #Otherwise, set that token to one
                token_count[token] = 1
        #Error Handling
        except Exception as e:
            print(f"Error processing token '{token}': {e}")
            continue
    #Return the count of the tokens
    return token_count

#Time Complexity: O(nlogn)
#Sorting is O(nlogn), where n is the number of unique tokens
#Must loop through sorted items to print: O(N)
#Function to print word frequency
#Source used: https://www.geeksforgeeks.org/python-sorted-function/
def print_frequencies(frequencies):
    #Print the words in order
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    for token, freq in sorted_frequencies:
        print(f"{token} => {freq}")

#Used discussion slides as source
if __name__ == '__main__':
    #Error handling
    if len(sys.argv) < 2:
        print("Format: python PartA.py <file>")
        #Exit with a non-zero if there is an error
        sys.exit(1)
    #Get filepath
    filepath = sys.argv[1]
    # Tokenize
    tokens = tokenize_file(filepath)
    # Get frequencies
    frequencies = token_frequency(tokens)
    #Print frequencies
    print_frequencies(frequencies)
