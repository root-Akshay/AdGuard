#! /bin/sh

url1="https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt"
url2="https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt"
sudo wget -qO- $url1 > Blacklists/domains.txt
echo "Domains Downloaded"
sudo wget -qO- $url2 > Blacklists/hostnames.txt
echo "Hostnames Downloaded"
sudo service dnsmasq restart
echo "Complete"
