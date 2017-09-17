# colors
source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

# These are packages that are installed using sudo apt-get
echo -e "\n${B_CYAN}${BEGIN}packages.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}Arduino IDE.${NC}"
sudo apt-get install -y arduino
echo -e "${B_YELLOW}${FINISH}Arduino IDE.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}Libudev API.${NC}"
sudo apt-get install -y libudev-dev
echo -e "${B_YELLOW}${FINISH}Libudev API.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}NMAP (network mapper tool).${NC}"
sudo apt-get install -y nmap
echo -e "${B_YELLOW}${FINISH}NMAP (network mapper tool).${NC}"

echo -e "\n${B_YELLOW}${BEGIN}Matplotlib.${NC}"
sudo apt-get install -y python3-matplotlib
echo -e "${B_YELLOW}${FINISH}Matplotlib.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}Requests.${NC}"
sudo apt-get install -y python3-requests
echo -e "${B_YELLOW}${FINISH}Requests.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}1-wire thermosensor.${NC}"
sudo apt-get install -y python3-w1thermsensor
echo -e "${B_YELLOW}${FINISH}1-wire thermosensor.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}xclip, comand-line copy+paste.${NC}"
sudo apt-get install -y xclip
echo -e "${B_YELLOW}${FINISH}xclip.${NC}"

echo -e "\n${B_YELLOW}${BEGIN}xscreensaver.${NC}"
sudo apt-get install -y xscreensaver
echo -e "${B_YELLOW}${FINISH}xscreensaver.${NC}"

echo -e "\n${B_CYAN}${FINISH}packages.${NC}"
