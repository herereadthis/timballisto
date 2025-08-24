# colors
source ./install_scripts/bash_colors.sh

echo -e "\n\n${CYAN}Welcome to Lutra.${NC}"
echo -e "${CYAN}Raspberry Pi setup by @herereadthis.${NC}\n\n"

echo -e "${B_CYAN}Ensure Raspbian and packages are up-to-date${NC}"
sudo apt-get -y update
sudo apt-get -y upgrade
echo -e "${B_CYAN}Raspian is up-to-date!.${NC}"

# install packages using apt-get install
./install_scripts/package_install.sh

# install packages using pip install
./install_scripts/pip_packages.sh

echo -e "\n${CYAN}Copying kernal modules for booting.${NC}"
sudo cp ./modules /etc/modules
echo -e "\n${CYAN}Kernal modules for booting are ready to use.${NC}"

echo -e "\n${CYAN}Copying .pypirc.${NC}"
cat ./.pypirc >> ~/.pypirc
echo -e "\n${CYAN}Remember to update with your credentials!${NC}"

# copy bash aliases
echo -e "\n${CYAN}Copying bash aliases.${NC}"
cat ./.bash_aliases >> ~/.bash_aliases
echo -e "\n${CYAN}Bash aliases are ready to use.${NC}"

exec bash

