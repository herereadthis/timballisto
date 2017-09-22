source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

# install pip the right way, perhaps
echo -e "\n${CYAN}${BEGIN}pip.${NC}"
sudo pip uninstall pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
echo -e "${CYAN}${FINISH}pip.${NC}\n"

# these are packages that are installed using pip install
echo -e "\n${B_CYAN}${BEGIN}pip packages.${NC}"

PKG='anyone: sample PyPi package'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U anyone
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='gspread: Google Spreadsheets Python API'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U gspread
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='flake8: Python linter'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U flake8
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='oauth2client: OAuth 2.0 resource'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U oauth2client
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='scapy: packet manipulation'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U scapy-python3
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='speedtest-cli: bandwidth testor'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U speedtest-cli
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='twilio: SMS comunication'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U twilio
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='twine: PyPi utility'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U twine
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='virtualenv: Python Virtual Environments'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U virtualenv
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='virtualenvwrapper Virtual Environments Wrapper'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U virtualenvwrapper
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${B_CYAN}${FINISH}Pip Packages.${NC}"