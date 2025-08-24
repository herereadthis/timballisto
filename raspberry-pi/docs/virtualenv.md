# Python Virtual Environments

* When working with Python packages and projects, you may find that Project A depends on a certain version of a package, but Project B depends on a different version.
* So if you update your package to work with Project A, then Project B will be borked.
* Do your stuff in virtual environments to avoid this problem. What you are really doing is isolating Project A from Project B. 

## Installation

```bash
# virtualenv creates isolated Python enviroments
sudo pip install virtualenv
# provides a set of commands to make working with virtualenv easier
sudo pip install virtualenvwrapper
```

## Usage


```bash
# Make your directory
mkdir my_project
cd my_project

# Create virtualenv
# A folder will be created which will contain the environment
virtualenv my_project

# Activate the virtual environment
source my_project/bin/activate

# Deactivte the virtual environment
deactivate

# Deleting the virtual environment is straightforward
rm -rf my_project


# virtualenvwrapper can help you manage all the virtual environments
# Initialize the virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

# Create a virtual environment
# This time, a new folder won't be created.
# Instead it will be located in a central .virtualenvs directory
mkvirtualenv my_project

# work on the project
workon my_project

# cd into the virtual environment e.g., view bin, lib
cdvirtualenv

# quit the project
deactivate

# delete the virtual environment
rmvirtualenv my_project

# list all virtual environments
lsvirtualenv

```
