# colors
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
LCYAN='\033[1;36m'
NC='\033[m'
CURRENT_DIR=${PWD}

BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n\n${CYAN}Welcome to Lutra.${NC}"
echo -e "${CYAN}Github Repositories setup by @herereadthis.${NC}\n\n"

echo -e "\n${LCYAN}Begin cloning packages.${NC}"

PKG='Dropbox uploader'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
# Dropbox-Uploader/
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${LCYAN}Finish cloning packages.${NC}"


mkdir -p ~/repos;
cd ~/repos