Free WEBPanels for server management
✅✳️❎⚠️❌⭕️

1. CloudPanel
2. Ajenti
3. ISPConfig
4. Aapanel
✳️ Vesta CP
```bash
apt update && apt install -y wget curl
mkdir -p /temp && cd /temp ;
# Download installation script
bash <(curl http://vestacp.com/pub/vst-install.sh || wget -O - http://vestacp.com/pub/vst-install.sh)

# Download installation script
# DEFAULT:
#curl -O http://vestacp.com/pub/vst-install.sh && bash vst-install.sh

# DEFAULT + select modules:
read -p "Enter hostname: " WEBPanelHostname
read -p "Enter Admin Email: " WEBPanelEmail
read -p "Enter Admin Password: " WEBPanelPassword

bash <(curl http://vestacp.com/pub/vst-install.sh || wget -O - http://vestacp.com/pub/vst-install.sh) \\
  --nginx yes --apache yes --phpfpm no --named yes \\
  --remi yes \\
  --vsftpd no --proftpd yes \\
  --iptables yes --fail2ban yes \\
  --quota no \\
  --exim yes --dovecot yes --spamassassin yes --clamav yes --softaculous yes \\
  --mysql yes --postgresql yes \\
  --hostname ${WEBPanelHostname} --email ${WEBPanelEmail} --password ${WEBPanelPassword}
# 
# _________
# 
# URL: – https://your-host:8443
# 
# END
```

- Froxlor
- Virtualmin
- Zpanel
- FastPanel

✅ Plesk
```
sh <(curl https://autoinstall.plesk.com/one-click-installer || wget -O - https://autoinstall.plesk.com/one-click-installer)

# _________
# URL: – https://your-host:8443

# END
```

Control Web Panel
DirectAdmin
Solid CP
MediaCP


платных для управления сервером
cPanel
