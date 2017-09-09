# colors
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[m'

BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n${CYAN}Welcome to Lutra.${NC}\n"

# install pip the right way, perhaps
echo -e "${CYAN}Begin installing pip.${NC}"
sudo pip uninstall pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
echo -e "${CYAN}Finished installing pip.${NC}\n"

echo -e "\n${YELLOW}Begin installing xscreensaver.${NC}"
sudo apt-get install -y xscreensaver
echo -e "${YELLOW}Finished installing xscreensaver.${NC}"

echo -e "\n${YELLOW}${BEGIN}Requests.${NC}"
sudo apt-get install -y python3-requests
echo -e "${YELLOW}${FINISH}Requests.${NC}"

echo -e "\n${YELLOW}Begin installing Matplotlib.${NC}"
sudo apt-get install -y python3-matplotlib
echo -e "${YELLOW}Finished installing Matplotlib.${NC}"


# necessary installs

# copy bash aliases
echo -e "${CYAN}Copying bash aliases${NC}"
cat ./.bash_aliases >> ~/.bash_aliases
exec bash
