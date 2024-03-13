# File Renamer

Preface: it's amazing what ChatGPT can do

## Commands

### String Replace

* To use the `replace_string` script from the command line:
  ```shell
  python replace_string.py <directory> <match> <replacement>
  ```
* Replace `<directory>` with the path to the directory containing the files you want to rename, `<match>` with the string
you want to replace, and `<replacement>` with the string that will replace `<match>`.
* For example, if you want to replace all occurrences of the string "foo" with "bar" in all files in the directory 
`/path/to/files`, you would run the following command:
  ```shell
  python replace_string.py /path/to/files foo bar
  ```

### Remove Characters

* To use the `remove_chars` script from the command line:
  ```shell
  python remove_chars.py <directory> <count> <start|end>
  ```
* Replace `<directory>` with the path to the directory containing the files you want to rename, `<count>` with the number of characters to remove, and `<start|end>` with either "start" or "end" depending on whether the characters to be removed are at the beginning or end of the file name.
* For example, if you want to remove the first 3 characters from the names of all files in the directory `/path/to/files`, you would run the following command:
  ```shell
  python remove_chars.py /path/to/files 3 start
  ```
* If you wanted to remove the last 4 characters instead, you would run:
  ```shell
  python remove_chars.py /path/to/files 4 end
  ```

### Add String

* To use the `add_string` script from the command line:
  ```shell
  python add_string.py <directory> <string> <count> <start|end>
  ```
* Replace 
  * `<directory>` with the path to the directory containing the files you want to rename, 
  * `<string>` with the string you want to add to the file names, 
  * `<count>` with the number of characters from either the beginning or end of the file name that you want to keep, and
  * `<start|end>` with either "start" or "end" depending on whether you want to keep the first or last characters of the file name.
* For example, if you want to add the string "new_" to the beginning of all file names in the directory `/path/to/files` and keep the first 3 characters of the original file names, you would run the following command:
  ```shell
  python add_string.py /path/to/files new_ 3 start
  ```
* If you wanted to add the string "_old" to the end of all file names and keep the last 4 characters of the original file names instead, you would run:
  ```shell
  python add_string.py /path/to/files _old 4 end
  ```

  ## Notes

  ChatGPT Prompt:

  > write a pep-8 valid and pylint-valid python package that can be uploaded to and from pypi. In this package, it should have a replace_string.py script that renames files in a directory by taking three terminal inputs: the directory containing the files, the string to match and the string that replaces the match. It should also have another add_string.py script that renames files by taking 4 terminal inputs: the directory containing the files, a string to add, and number of characters from either the end or beginning of the file name. It should also have another remove_chars.py script that renames files by taking 4 terminal inputs: the directory containing the files, the number of characters to remove, and number of characters from either the end or beginning of the file name.