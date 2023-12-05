Free WEBPanels for server management
✅✳️❎⚠️❌⭕️

## 1. CloudPanel
  ```bash
      # Login via SSH to the Server.
      #ssh -i path_to_your_private_key root@serverIpAddress
      # Update the system and install the required packages.
      apt update && apt -y upgrade && apt -y install curl wget sudo

      # Run the installer with your preferred Database Engine.
      # installer MySQL 8.0
      curl -sS https://installer.cloudpanel.io/ce/v2/install.sh -o install.sh; \
        echo "85762db0edc00ce19a2cd5496d1627903e6198ad850bbbdefb2ceaa46bd20cbd install.sh" | \
        sha256sum -c && sudo CLOUD=hetzner bash install.sh

      # installer MariaDB 10.11
      #curl -sS https://installer.cloudpanel.io/ce/v2/install.sh -o install.sh; \
      #  echo "85762db0edc00ce19a2cd5496d1627903e6198ad850bbbdefb2ceaa46bd20cbd install.sh" | \
      #  sha256sum -c && sudo CLOUD=hetzner DB_ENGINE=MARIADB_10.11 bash install.sh

      # installer MariaDB 10.6
      #curl -sS https://installer.cloudpanel.io/ce/v2/install.sh -o install.sh; \
      #  echo "85762db0edc00ce19a2cd5496d1627903e6198ad850bbbdefb2ceaa46bd20cbd install.sh" | \
      #  sha256sum -c && sudo CLOUD=hetzner DB_ENGINE=MARIADB_10.6 bash install.sh

      # SECURITY
      # For security reasons, access CloudPanel as fast as possible to create the admin user. There is a small time window where bots can create the user. It's highly recommended to open port 8443 only for your IP via firewall.
      # 
      #Ignore the self-signed certificate warning and click on Advanced and Proceed to continue to CloudPanel.
      #
      # ************
      # URL: – [https://your-host:80](https://serverIpAddress:8443)
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
  # DEFAULT:
      ```bash
      apt update && apt install -y wget curl
      mkdir -p /temp && cd /temp ;
      
      # Download installation script
      curl -O http://vestacp.com/pub/vst-install.sh && chmod +x vst-install.sh && bash vst-install.sh
    ```

  # DEFAULT + select modules:
    ```bash
        apt update && apt install -y wget curl;
        mkdir -p /temp && cd /temp ;
    
        read -p "Enter hostname: " WEBPanelHostname
        read -p "Enter Admin Email: " WEBPanelEmail
        read -p "Enter Admin Password: " WEBPanelPassword
    
        bash <(curl http://vestacp.com/pub/vst-install.sh || wget -O - http://vestacp.com/pub/vst-install.sh) \
          --nginx yes --apache yes --phpfpm no --named yes \
          --remi yes \
          --vsftpd no --proftpd yes \
          --iptables yes --fail2ban yes \
          --quota no \
          --exim yes --dovecot yes --spamassassin yes --clamav yes --softaculous yes \
          --mysql yes --postgresql yes \
          --hostname ${WEBPanelHostname} --email ${WEBPanelEmail} --password ${WEBPanelPassword}
    
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

