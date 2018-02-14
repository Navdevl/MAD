#!/bin/bash

mkdir -p ~/.medium
cp medium_audio.py ~/.medium/medium_audio.py

GREEN='\033[0;32m'
NC='\033[0m' 


echo "COPY THIS FOLLOWING LINE TO YOUR BASHRC or ZSHRC"

echo -e "${GREEN}

getMediumAudio() {
  if [ -z \"\$1\" ] 
    then
      echo -e \"\${RED}Who the hell will pass the URL ?\"
      ec=0 # determine the desired exit code
      return \$ec 2>/dev/null || exit \$ec
  fi
  CURRENT_DIR=$(pwd)
  MEDIUM_PYTHON_SCRIPT=~/.medium/medium_audio.py
  python \$MEDIUM_PYTHON_SCRIPT \$1 \$CURRENT_DIR
}

alias getMedium=getMediumAudio ${NC}"

echo ""
echo "Reload your bashrc or zshrc configuration after pasting. "




