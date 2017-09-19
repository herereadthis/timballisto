# colors
source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

# These are packages that are installed using sudo apt-get
echo -e "\n${B_CYAN}${BEGIN}packages.${NC}"

PKG='Arduino IDE'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y arduino
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='I2C programming library'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libi2c-dev
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='Libudev API'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y libudev-dev
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='NMAP (network mapper tool)'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y nmap
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='Matplotlib'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y python3-matplotlib
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='Requests'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y python3-requests
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='1-wire thermosensor'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y python3-w1thermsensor
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='xclip, comand-line copy+paste'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y xclip
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='xscreensaver'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y xscreensaver
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${B_CYAN}${FINISH}packages.${NC}"
