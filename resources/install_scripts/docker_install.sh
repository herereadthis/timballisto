source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n${B_CYAN}${BEGIN} Docker.${NC}"

echo -e "\n${B_YELLOW}Begin downloading Docker client.${NC}"
curl -sSL https://get.docker.com | sh
echo -e "${B_YELLOW}Finish downloading Docker client.${NC}"

PKG='mara'
echo -e "\n${B_YELLOW}${BEGIN}${PKG} client.${NC}"
docker pull herereadthis/$PKG
echo -e "${B_YELLOW}${FINISH}${PKG} client.${NC}"

PKG='raspberry-pi-hello-world'
echo -e "\n${B_YELLOW}${BEGIN}${PKG} client.${NC}"
docker pull herereadthis/$PKG
echo -e "${B_YELLOW}${FINISH}${PKG} client.${NC}"

echo -e "\n${B_YELLOW}Begin cleanup.${NC}"
echo -e "${GREEN}Set Docker to auto-start.${NC}"
sudo systemctl enable docker
echo -e "${GREEN}Enable Docker client to be used by root user.${NC}"
sudo usermod -aG docker pi
echo -e "${GREEN}Confirm everything is working.${NC}"
docker run herereadthis/raspberry-pi-hello-world
echo -e "${B_YELLOW}Finish cleanup.${NC}"

echo -e "\n${B_CYAN}${FINISH} Docker.${NC}"