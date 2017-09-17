# colors
source ./bash_colors.sh

CURRENT_DIR=${PWD}

BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n\n${BCYAN}Welcome to Lutra.${NC}"
echo -e "${BCYAN}Github Repositories setup by @herereadthis.${NC}\n"

echo -e "\n${LCYAN}Begin cloning packages.${NC}"

echo -e "\n${PURPLE}Current working directory: ${PWD}${NC}"

mkdir -p ~/repos
cd ~/repos

echo -e "\n${PURPLE}Repos directory: ${PWD}${NC}"

PKG='Dropbox uploader'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
# Dropbox-Uploader/
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='anyone: sample PyPi package'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
git clone https://github.com/herereadthis/anyone.git
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='raspberry-pi-hello-world: sample docker image'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
git clone https://github.com/herereadthis/raspberry-pi-hello-world.git
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${LCYAN}Finish cloning packages.${NC}"

cd $CURRENT_DIR

echo -e "\n${PURPLE}Back to previous directory: ${PWD}${NC}"
