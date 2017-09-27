source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '
TITLE='Mosquitto MQTT'

echo -e "\n${B_CYAN}${BEGIN}${TITLE}.${NC}"

echo -e "\n${B_YELLOW}Begin getting latest version of broker.${NC}"
sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
rm -rf mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list
echo -e "${B_YELLOW}Finish getting latest version of broker.${NC}"

echo -e "\n${B_YELLOW}Begin installing MQTT broker.${NC}"
sudo apt-get install -y mosquitto
cd $CURRENT_DIR
echo -e "${B_YELLOW}Finish installing MQTT broker.${NC}"

PKG='mosquitto-clients: command line clients'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y mosquitto-clients
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

PKG='python-mosquitto: Python language bindings'
echo -e "\n${B_YELLOW}${BEGIN}${PKG}.${NC}"
sudo apt-get install -y python-mosquitto
echo -e "${B_YELLOW}${FINISH}${PKG}.${NC}"

# stop the broker, as it has immediately started.
sudo /etc/init.d/mosquitto stop

echo -e "\n${B_CYAN}${FINISH}${TITLE}.${NC}"
