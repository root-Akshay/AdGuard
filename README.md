# AdGuard
AdGuard is dnsmasq based adblocker with a Web UI to monitor stats. Get rid of annoying ads protect your devices from pesky malware. Make your web surfing fast, secure and ad-free.

# Installation
First, clone the repository on to your Raspberry Pi  
```bash git clone https://github.com/root-Akshay/AdGuard.git ```  

After the cloning completes,    
Open the AdGuard Directory:  

```bash cd AdGuard ```  

Convert the install file to an executable file:\
```bash sudo chmod +x install.sh ```  

Run the file, it will install Adguard and other Required Dependencies.  
```bash ./install.sh ```  

System will reboot after installation completes  

# Running AdGuard  
To start AdGuard:  
```bash sudo systemctl start adguard ```  

To stop AdGuard:  
```bash sudo systemctl stop adguard ```  

# Web Interface  
The install.sh script gives your RPI a static IP 192.168.0.200.  

To access the web Panel. Open chrome and type RPI in search bar.  
``` 192.168.0.200/login ```  

Enter the Id and Password::  
```
Id: Adguard
Pass::Adguard123
```
# Features
* Easy To Install 
* Lightweight 
* Web Panel 
* Responsive 
* Free 


# Screenshots
![](Screenshots/Login.png) ![](Screenshots/Stats2.png) ![](Screenshots/Stats3.png)

# Credits
Hero Icons (https://heroicons.com/) 

