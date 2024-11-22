#!/bin/bash

red="\033[31m"
reset="\033[0m"

dependencies="[+] Installing dependencies."

for ((i=0; i<${#dependencies}; i++)); do
    echo -n -e "${red}${dependencies:$i:1}${reset}"
    sleep 0.05
done
echo ""

md5sum="Installing ucommon-utils..."

for ((i=0; i<${#md5sum}; i++)); do
    echo -n -e "${red}${md5sum:$i:1}${reset}"
    sleep 0.05
done
echo ""
sudo apt install -y ucommon-utils

exiftool="Installing exiftool..."
for ((i=0; i<${#exiftool}; i++)); do
    echo -n -e "${red}${exiftool:$i:1}${reset}"
    sleep 0.05
done
echo ""
sudo apt install -y exiftool
echo ""
