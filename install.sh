#!/bin/bash
clear
apt update -y
apt upgrade -y
apt install git
apt install python3

python3 install.py
