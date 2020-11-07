#!/bin/bash
sudo cat >> /etc/dhcpcd.conf << EOF

interface eth0
static ip_address=192.168.0.201/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

interface wlan0
static ip_address=192.168.0.200/24
static routers=192.168.0.1
static domain_name_servers=1.1.1.1 1.0.0.1
EOF

echo "Done. Rebooting..."
sleep 5
sudo reboot
