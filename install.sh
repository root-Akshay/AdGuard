
#!/bin/bash
echo "Installing Dnsmasq"
sudo apt-get install dnsmasq
sudo rm /etc/dnsmasq.conf
echo "Configuring Dnsmasq"

sudo tee -a /etc/dnsmasq.conf  > /dev/null <<EOT
no-dhcp-interface=eth0
cache-size=1000
domain-needed
bogus-priv
dns-forward-max=150
no-poll
log-queries
log-facility=/var/log/dnsmasq.log
conf-file=home/pi/AdGu@rd/Blacklists/domains.txt
addn-hosts=home/pi/AdGu@rd/Blacklists/hostnames.txt
EOT

echo "Downloading Blacklists"

sudo chmod +x updateblacklist.sh
sudo chmod +x adgu@rd.sh
echo "`./updateblacklist.sh`"

echo "Restarting Dnsmasq"
sudo systemctl daemon-reload
sudo systemctl restart dnsmasq

echo "Installing Python3"
sudo apt-get install python3

echo "Installing Flask"
pip3 install Flask

sudo chmod +x setstaticip.sh
echo "`./setstaticip.sh`"
