# colors
source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n\n${CYAN}Welcome to Lutra.${NC}"
echo -e "${CYAN}RTL-SDR setup by @herereadthis.${NC}\n\n"

echo -e "\n${B_CYAN}${BEGIN}packages.${NC}"

PKG='libqt5core5a: core module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libqt5core5a
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='libqt5gui5: GUI module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libqt5gui5
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='libqt5network5: network module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libqt5network5
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='libqt5widgets5: widgets module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libqt5widgets5
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='libqt5svg5: SVG module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libqt5svg5
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='libportaudio2: portable audio module'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libportaudio2
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${B_CYAN}${FINISH}packages.${NC}"

echo -e "\n${B_CYAN}${BEGIN} GQRX.${NC}"

echo -e "\n${B_YELLOW}Begin cloning Github repository in ~/repos.${NC}"
mkdir -p ~/repos
cd ~/repos
wget https://github.com/csete/gqrx/releases/download/v2.6/gqrx-2.6-rpi3-2.tar.xz
tar xvf gqrx-2.6-rpi3-2.tar.xz
rm -rf gqrx-2.6-rpi3-2.tar.xz
echo -e "\n${B_YELLOW}Finished cloning Github repository in ~/repos.${NC}"

echo -e "\n${B_YELLOW}Begin setup.${NC}"
./gqrx-2.6-rpi3-2/setup_gqrx.sh
cd $CURRENT_DIR
echo -e "\n${B_YELLOW}Finish setup.${NC}"


echo -e "\n${B_CYAN}${FINISH}GQRX.${NC}"

