# colors
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
LCYAN='\033[1;36m'
NC='\033[m'

BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n\n${CYAN}Welcome to Lutra.${NC}"
echo -e "${CYAN}Raspberry Pi setup by @herereadthis.${NC}\n\n"

echo -e "${LCYAN}Ensure Raspbian and packages are up-to-date${NC}"
sudo apt-get -y update
sudo apt-get -y upgrade
echo -e "${LCYAN}Raspian is up-to-date!.${NC}"

# install pip the right way, perhaps
echo -e "\n${CYAN}${BEGIN}pip.${NC}"
sudo pip uninstall pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
echo -e "${CYAN}${FINISH}pip.${NC}\n"

echo -e "\n${LCYAN}${BEGIN}packages.${NC}"

echo -e "\n${YELLOW}${BEGIN}Arduino IDE.${NC}"
sudo apt-get install -y arduino
echo -e "${YELLOW}${FINISH}Arduino IDE.${NC}"

echo -e "\n${YELLOW}${BEGIN}Libudev API.${NC}"
sudo apt-get install -y libudev-dev
echo -e "${YELLOW}${FINISH}Libudev API.${NC}"

echo -e "\n${YELLOW}${BEGIN}NMAP (network mapper tool).${NC}"
sudo apt-get install -y nmap
echo -e "${YELLOW}${FINISH}NMAP (network mapper tool).${NC}"

echo -e "\n${YELLOW}${BEGIN}Matplotlib.${NC}"
sudo apt-get install -y python3-matplotlib
echo -e "${YELLOW}${FINISH}Matplotlib.${NC}"

echo -e "\n${YELLOW}${BEGIN}Requests.${NC}"
sudo apt-get install -y python3-requests
echo -e "${YELLOW}${FINISH}Requests.${NC}"

echo -e "\n${YELLOW}${BEGIN}1-wire thermosensor.${NC}"
sudo apt-get install -y python3-w1thermsensor
echo -e "${YELLOW}${FINISH}1-wire thermosensor.${NC}"

echo -e "\n${YELLOW}${BEGIN}xclip, comand-line copy+paste.${NC}"
sudo apt-get install -y xclip
echo -e "${YELLOW}${FINISH}xclip.${NC}"

echo -e "\n${YELLOW}${BEGIN}xscreensaver.${NC}"
sudo apt-get install -y xscreensaver
echo -e "${YELLOW}${FINISH}xscreensaver.${NC}"

echo -e "\n${LCYAN}${FINISH}packages.${NC}"

echo -e "\n${LCYAN}${BEGIN}pip packages.${NC}"

PKG='anyone: sample PyPi package'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U anyone
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='gspread: Google Spreadsheets Python API'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U gspread
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='flake8: Python linter'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U flake8
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='oauth2client: OAuth 2.0 resource'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U oauth2client
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='scapy: packet manipulation'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U scapy-python3
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='speedtest-cli: bandwidth testor'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U speedtest-cli
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='twilio: SMS comunication'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U twilio
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='twine: PyPi utility'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U twine
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='virtualenv: Python Virtual Environments'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U virtualenv
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

PKG='virtualenvwrapper Virtual Environments Wrapper'
echo -e "\n${YELLOW}${BEGIN}${PKG}.${NC}"
sudo pip3 install -U virtualenvwrapper
echo -e "${YELLOW}${FINISH}${PKG}.${NC}"

echo -e "\n${LCYAN}${FINISH}Speedtest.${NC}"

# copy bash aliases
echo -e "\n${CYAN}Copying bash aliases.${NC}"
cat ./.bash_aliases >> ~/.bash_aliases
echo -e "\n${CYAN}Bash aliases are ready to use.${NC}"

exec bash

