# Z Shell Zsh

```zsh
# install zsh
sudo apt-get install zsh
# set as default shell
chsh -s /bin/zsh
# whoops set it back to bash?
chsh -s /bin/bash
# install oh my zsh
# See also https://github.com/ohmyzsh/ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Aliases

```zsh
# navigation
alias ls="ls -a"
alias ~='cd ~/'
alias ..='cd ../'
alias desk='cd ~/Desktop'
alias g='cd ~/git' # Navigate to location of repositories

# Github commands
alias cfr='git checkout master;git fetch --all;git reset --hard origin/master'
alias rmain='git checkout main;git fetch --all;git reset --hard origin/main'
alias gb='git branch'
alias gs='git status'
alias gmm='git merge master'

# Delete Branches
function gbd () {
        git branch -D $1 $2 $3 $4 $5 $6
}
# Commit all changes
function gca () {
        git commit -am \"$1\"
}
# Checkout a local branch
function gc () {
        git checkout $1
}
# Create a new branch
function gcb () {
    git checkout -b $1
}
# Push a branch
function gpo () {
    git push origin $1
}
# Reset a branch to the lastest remote
function gr () {
    git fetch origin;git reset --hard origin/$1
}
```