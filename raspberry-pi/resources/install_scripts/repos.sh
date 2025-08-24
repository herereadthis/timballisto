# colors
source ./bash_colors.sh

CURRENT_DIR=${PWD}
BEGIN='Begin installing '
FINISH='Finished installing '

echo -e "\n\n${B_CYAN}Welcome to Lutra.${NC}"
echo -e "${B_CYAN}Github Repositories setup by @herereadthis.${NC}\n"

# echo -e "\n${B_CYAN}Begin cloning packages.${NC}"

echo -e "\n${PURPLE}Current working directory: ${PWD}${NC}"

mkdir -p ~/repos
cd ~/repos

echo -e "\n${PURPLE}Repos directory: ${PWD}${NC}"
