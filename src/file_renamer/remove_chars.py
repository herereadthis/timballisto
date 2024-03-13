import os
import sys

def remove_chars(num_chars, position):
    for filename in os.listdir("."):
        if filename.endswith(".txt"):
            if position == "beginning":
                new_filename = filename[num_chars:]
            elif position == "end":
                new_filename = filename[:-num_chars]
            os.rename(filename, new_filename)

if __name__ == "__main__":
    num_chars = int(sys.argv[1])
    position = sys.argv[2]
    remove_chars(num_chars, position)
