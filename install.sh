#!/bin/bash

USERID=`id -u`

if [ $USERID -ne 0 ]; then
    exec sudo bash $0
fi

pacman -Syu -- < packages.arch.txt

systemctl enable cups.service
systemctl start cups.service