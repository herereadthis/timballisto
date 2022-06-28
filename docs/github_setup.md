# How To Set Up Github On Your Raspberry Pi

* Github is repository hosting service. Users create repositories of code or whatever they want.
* Github allows for version control, so users can go back and forward in the history of their code.
* Additionally, other users - or collaborators - can contribute code to the respository.
* Github is the most popular and widely used way to share code.

## Setup

```bash
sudo apt-get install git
```

* Create an account at Github if you don&rsquo;t have one already. Add your configuration (use your own credentials):
  ```bash
  git config --global user.name "herereadthis"
  git config --global user.email "herereadthis@email.com"
  # list configs
  git config -l
  ```

### Personal Access Token

* Go to Github > Settings > Developer Settings > Personal Access Token
* Generate a personal access token at the level you need. Copy the PAT.
* Clone some repository that you control, then push a branch
* Enter your username
* Paste the PAT as the password

```bash
# Cache the credentials
git config --global credential.helper cache
# Delete the credentials
git config --global --unset credential.helper
```

### ~SSH Setup~ Outdated

*Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.*

* Create hidden ssh directory
  ```bash
  cd ~
  mkdir .ssh
  ```
* Generate SSH key. Use your own email!
  Instructions here: [github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Add SSH key to your github account, [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
* Test your connection:
  ```bash
  ssh -T git@github.com
  # verify by typing yes
  ```
* Remember when cloning a repo, use the `git@github` method
* Recommended: make a repos folder at home to contain all repositories
  ```bash
  mkdir -p ~/git
  ```
