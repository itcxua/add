Free WEBPanels for server management
✅✳️❎⚠️❌⭕️

## 1. CloudPanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 2. Ajenti


## 3. ISPConfig
  ```bash
      sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
      #
      # ************
      # URL: – https://your-host:8090
      #
      # ****** END
  ```

## 4. CyberPanel
  ```bash
      sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
      #
      # ************
      # URL: – https://your-host:8090
      #
      # ****** END
  ```

## 5. Aapanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 6. Froxlor
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 7. Virtualmin
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 8. Zpanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 9. FastPanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 10. Control Web Panel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 11. DirectAdmin
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 12. Solid CP
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 13. MediaCP
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 14. Vesta CP
  ```bash
      apt update && apt install -y wget curl
      mkdir -p /temp && cd /temp ;
      
      # Download installation script
      bash <(curl http://vestacp.com/pub/vst-install.sh || wget -O - http://vestacp.com/pub/vst-install.sh)
      
      # Download installation script
      # DEFAULT:
      #curl -O http://vestacp.com/pub/vst-install.sh && chmod +x vst-install.sh && bash vst-install.sh
      
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
      # ************
      # URL: – https://your-host:8443
      #
      # END
  ```

_____________________________________________________________




платных для управления сервером
1. cPanel
2. Plesk
   ```
   sh <(curl https://autoinstall.plesk.com/one-click-installer || wget -O - https://autoinstall.plesk.com/one-click-installer)

   # _________
   # URL: – https://your-host:8443

   # END
   ```

