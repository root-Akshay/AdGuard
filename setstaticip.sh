#!/bin/bash
sudo cat >> /etc/network/interfaces << EOF

auto enp0s3
iface enp0s3 inet static
    address 192.168.1.28
    gateway 192.168.1.1
    netmask 255.255.255.0
    network 192.168.1.0
    broadcast 192.168.1.255
EOF
