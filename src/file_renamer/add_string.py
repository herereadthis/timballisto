import os
import argparse


def add_string(directory: str, add_str: str, num_chars: int, position: str) -> None:
    """Adds a string to file names based on the given arguments.

    Args:
        directory (str): The directory containing the files.
        add_str (str): The string to add to the file names.
        num_chars (int): The number of characters to extract from the file names.
        position (str): The position to add the string. Must be either "start" or "end".
    """
    # Get the list of files in the specified directory
    files = os.listdir(directory)

    # Loop through each file and add the string to its name
    for file in files:
        # Get the file name without the extension
        name, ext = os.path.splitext(file)

        # Determine the position to add the string
        if position == 'start':
            new_name = add_str + name[:num_chars] + ext
        elif position == 'end':
            new_name = name[:-num_chars] + add_str + ext
        else:
            raise ValueError('Position argument must be either "start" or "end".')

        # Rename the file
        print(file)
        print(new_name)
        # os.rename(os.path.join(directory, file), os.path.join(directory, new_name))


if __name__ == '__main__':
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='Add a string to file names')
    parser.add_argument('directory', type=str, help='The directory containing the files')
    parser.add_argument('add_str', type=str, help='The string to add to the file names')
    parser.add_argument('num_chars', type=int, help='The number of characters to extract from the file names')
    parser.add_argument('position', type=str, help='The position to add the string. Must be either "start" or "end".')

    args = parser.parse_args()

    # Call the add_string function with the specified arguments
    add_string(args.directory, args.add_str, args.num_chars, args.position)
