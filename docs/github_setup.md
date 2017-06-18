# How To Set Up Github On Your Raspberry Pi

Github is repository hosting service. Users create repositories of code or 
whatever they want. Github allows for version control, so users can go back and
forward in the history of their code. Additionally other users - or
collaborators - can contribute code to the respository. Github is the most
popular and widely used way to share code.

### Set up Github

```bash
git config --global user.name "herereadthis"
git config --global user.email "herereadthis@email.com"

# Generate Github SSH keys
cd ~
mkdir .ssh
cd .ssh
ssh-keygen -t rsa -b 4096 -C "herereadthos@email.com"
# you will be prompted to create a file; the id_rsa default is fine
# you will also be prompted to create a passphrase; create it
# start the ssh-agent
eval "$(ssh-agent -s)"
# add SSH private key to the ssh-agent
ssh-add id_rsa
#copy the SSH key
xclip -sel clip < id_rsa.pub
```

Log in to your github page, then go to [/settings/keys](https://github.com/settings/keys), 
and select "New SSH key." Paste your key there and save.

```bash
# test your connection
ssh -T git@github.com
# verify by typing yes
```