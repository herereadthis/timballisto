"""This script will download stuff for you."""

import urllib.request
import io
import gzip
import os


def create_dirs(output_path):
    """Create directory and sub-folders, if they do not exist."""
    # help from https://stackoverflow.com/questions/273192/
    directory = os.path.dirname(output_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_file_and_unzip(file_url, output_path):
    """Download gzip file and puts in appropriate directory."""
    # help from https://stackoverflow.com/questions/15352668/
    create_dirs(output_path)

    response = urllib.request.urlopen(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    # 'rb' is mode, -r means read, -w means write, -b means open in binary mode
    # for cross-platform portability
    with open(output_path, 'wb') as outfile:
        outfile.write(decompressed_file.read())


# Check to see if this file is run as a module (import) or not
if __name__ == '__main__':
    get_file_and_unzip(
        'http://bulk.openweathermap.org/sample/city.list.json.gz',
        'downloads/city.list.json'
    )
