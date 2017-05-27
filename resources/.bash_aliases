mcd () {
	mkdir $1;cd $1
}

alias ~='cd ~/'
alias ..='cd ../'
alias desk='cd ~/Desktop'

# git commands

alias cfr='git checkout master;git fetch --all;git reset --hard origin/master'
alias gpom='git push origin master'
alias gb='git branch'
alias gs='git status'
alias gmm='git merge master'

gbd () {
	git branch -D $1 $2 $3 $4 $5
}
gca () {
	git commit -a -m \"$1\"
}
gc () {
	git checkout $1
}
gcb () {
    git checkout -b $1
}
gpo () {
    git push origin $1
}