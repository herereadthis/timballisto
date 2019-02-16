# How To Set Up Github On Your Raspberry Pi

* Github is repository hosting service. Users create repositories of code or whatever they want.
* Github allows for version control, so users can go back and forward in the history of their code.
* Additionally, other users - or collaborators - can contribute code to the respository.
* Github is the most popular and widely used way to share code.

## Setup

* Create an account at Github if you don&rsquo;t have one already. Add your configuration (use your own credentials):
  ```bash
  git config --global user.name "herereadthis"
  git config --global user.email "herereadthis@email.com"
  ```
* Create hidden ssh directory
  ```bash
  cd ~
  mkdir .ssh
  ```
* Generate SSH key. User your own email!
  ```bash
  cd .ssh
  ssh-keygen -t rsa -b 4096 -C "herereadthis@email.com"
  ```
  * You will be prompted to create a file; the id_rsa default is fine
  * Y ou will also be prompted to create a passphrase; create it
* start the ssh-agent
  ```bash
  eval "$(ssh-agent -s)"
  ```
* Add SSH private key to the ssh-agent
  ```bash
  ssh-add id_rsa
  ```
* Copy the contents of the public key
  ```bash
  # show the contents
  cat ./id_rsa.pub
  # copy those contents
  ```
* Log in to your github page, then go to [/settings/keys](https://github.com/settings/keys), and select "New SSH key." Paste your key there and save.
* Test your connection:
  ```bash
  ssh -T git@github.com
  # verify by typing yes
  ```
* Remember when cloning a repo, use the `git@github` method
* Recommended: make a repos folder at home to contain all repositories
  ```bash
  mkdir -p ~/repos;cd ~/repos
  ```
* Finally! Clone this repo. It has lots of goodies
  ```bash
  git clone git@github.com:herereadthis/lutra.git
  ```
