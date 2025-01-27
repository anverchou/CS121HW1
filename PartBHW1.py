import PartAHW1 as A
import sys

#Time Complexity: O(n1 + n2)
#Construct token_count1: O(n1)
#Construct token_count2: O(n2)
#Find common tokens between the two dicts
#Find intersection of the two files
def intersection(filepath1, filepath2):
    try:
        # Convert token lists into dictionaries
        token_count1 = {}
        for token in file1_tokens:
            token_count1[token] = token_count1.get(token, 0) + 1

        token_count2 = {}
        for token in file2_tokens:
            token_count2[token] = token_count2.get(token, 0) + 1

        # Find common tokens and count occurrences
        common_tokens = []
        for token in token_count1:
            if token in token_count2:
                common_tokens.append(token)
        return common_tokens
    except Exception as e:
        print(f"Error while finding intersection: {e}")
        return []

#Used discussion slides as source for main
if __name__ == '__main__':
    #Error handling
    if len(sys.argv) < 3:
        print("Format: python PartBHW1.py <file1> <file2>")
        #Exit with a non-zero if there is an error
        sys.exit(1)
    try:
        #Get file paths
        filepath1 = sys.argv[1]
        filepath2 = sys.argv[2]
        #Tokensize the files
        file1_tokens = A.tokenize_file(filepath1)
        file2_tokens = A.tokenize_file(filepath2)
        #Get intersections between the two files
        common_tokens = intersection(file1_tokens, file2_tokens)
        #Print the number of intersections
        print(f"Intersections: {len(common_tokens)}")
    except IndexError:
        print("Error: Missing file path arguments")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)