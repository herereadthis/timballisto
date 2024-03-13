import os
import sys

def replace_string(directory, string_to_match, replacement_string):
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and string_to_match in filename:
            new_filename = filename.replace(string_to_match, replacement_string)
            os.rename(filename, new_filename)

if __name__ == "__main__":
    string_to_match = sys.argv[1]
    replacement_string = sys.argv[2]
    replace_string(string_to_match, replacement_string)
