source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

# These are packages that are installed using sudo apt-get
echo -e "\n${B_CYAN}${BEGIN} NodeJS.${NC}"

echo -e "\n${B_YELLOW}Begin downloading Node v6.11.3.${NC}"
wget https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-armv7l.tar.xz
echo -e "${B_YELLOW}Finish downloading Node v6.11.3.${NC}"

echo -e "\n${B_YELLOW}Begin extracting Node.${NC}"
tar xf node-v6.11.3-linux-armv7l.tar.xz
NV=$(node-v6.11.3-linux-armv7l/bin/node -v)
echo -e "\n${GREEN}Downloaded Node version is: ${NV}.${NC}"
echo -e "${B_YELLOW}Finish extracting Node.${NC}"

echo -e "\n${B_YELLOW}Begin copying Node to system.${NC}"
cd node-v6.11.3-linux-armv7l/
sudo cp -R * /usr/local/
echo -e "${B_YELLOW}Finish copying Node to system.${NC}"

echo -e "\n${B_YELLOW}Begin cleanup.${NC}"
cd $CURRENT_DIR
rm -rf node-v6*
export PATH=$PATH:/usr/local/bin
N_V=$(node -v)
NPM_V=$(node -v)
echo -e "\n${GREEN}Node version is: ${N_V}.${NC}"
echo -e "\n${GREEN}NPM version is: ${NPM_V}.${NC}"
echo -e "${B_YELLOW}Finish cleanup.${NC}"

echo -e "\n${B_CYAN}${FINISH}NodeJS.${NC}"