# Free WEBPanels for server management

*****************************
✅✳️❎⚠️❌⭕️🟢🟡✔️®️📶⁉️‼️⚠️❌⛔️⭕️🌐


## 🟢 1. CloudPanel

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

## 🟢 2. Ajenti

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 🟢 3. ISPConfig

  ```bash
      sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
      #
      # ************
      # URL: – https://your-host:8090
      #
      # ****** END
  ```


## 🟢 4. CyberPanel

### Установите CyberPanel на сервер Ubuntu 20.04 LTS

‼️ CyberPanel — это инструмент с открытым исходным кодом, который поддерживает различные операционные системы
‼️ OS: Ubuntu 22.04 LTS Server, CentOS 7/8, CloudLinux 7/8, Red Hat Enterprise Linux 6/7/8, Debian 9/10 и OpenSUSE 15.2.

🌐 URL: [CyberPanel Install Ubuntu 20.04](https://www.redswitches.com/blog/cyberpanel-on-ubuntu/#5)

⚠️ Ubuntu 20.04 - None Upgrade 22.04

  ```bash
      sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
      #
      # ************
      # URL: – https://your-host:8090
      #
      # ****** END
  ```

### Установите CyberPanel на сервер Ubuntu 22.04 LTS

⚠️ Ubuntu 22.04 - Upgrade 22.04

🌐 URL: [CyberPanel Install Ubuntu 22.04](https://www.redswitches.com/blog/cyberpanel-on-ubuntu/#5)

  ```bash
    # Первым шагом является вход на ваш сервер с помощью SSH-клиента, такого как PuTTY, и обновление системных пакетов:
    sudo apt-get update && sudo apt-get upgrade
    
    # Используйте следующую команду для установки зависимостей CyberPanel:
    sudo apt-get install python3 python3-dev python3-pip wget unzip rsync net-tools curl libssl-dev

    # Следующий скрипт подключится к официальному сайту и загрузит последнюю версию.
    sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)

    # Используйте следующую команду, чтобы открыть эти порты в брандмауэре.
    sudo ufw allow 8090/tcp && sudo ufw allow 8091/tcp
    sudo ufw allow 80,443,25,587,465,110,143,993,53,21/tcp
    sudo ufw allow 443,53/udp
    sudo ufw allow 40110:40210/tcp

  ```

#### Шаг № 1: Обновите системные пакеты
#### Шаг № 2: Установите зависимости
#### Шаг 3. Загрузите и установите CyberPanel.
#### Шаг №4: Выполните первоначальную настройку
  Далее установщик попросит вас выбрать подходящие параметры для продолжения установки.
  Вы можете выбрать опцию «1», чтобы установить панель управления CyberPanel на свой сервер. Если вы хотите выйти из установщика, выберите опцию «2».
  3 Установите Киберпанель

#### Шаг 5. Выберите подходящую версию CyberPanel.
  На следующем этапе текстовый установщик предложит вам выбрать версию для установки CyberPanel. Вы можете выбрать «OpenLiteSpeed» или «LiteSpeed ​​Enterprise» по вашему выбору.
  4 Первоначальная настройка Киберпанели

#### Шаг № 6: Установите полный сервис
  На этом этапе выберите полную службу CyberPanel для вашего сервера Ubuntu 22, включая PowerDNS, Postfix и Pure-FTPd.
  Нажмите Y, чтобы продолжить.
  5 установить полный сервис

#### Шаг № 7. Выберите локальную или удаленную настройку MySQL.
  Теперь вы увидите интересный выбор, связанный с сервером базы данных MySQL.
  CyberPanel одинаково хорошо работает с локальными и удаленными серверами MySQL, и вы можете выбрать сценарий, который работает с вашей серверной инфраструктурой.
  Итак, если вы в настоящее время используете отдельный сервер MySQL, вы можете выбрать опцию «Y», чтобы установщик не устанавливал службу MySQL на ваш сервер.
  Если вы хотите установить сервер MySQL на тот же сервер, вы можете выбрать опцию «N» и продолжить дальше. Вариант установки по умолчанию — «Нет», поэтому вы можете продолжить, если не хотите устанавливать локальный сервер MySQL.
  6 Удаленный MySQL

#### Шаг 8. Выберите версию CyberPanel.
  Установщик предлагает вам выбрать конкретную версию или просто установить последнюю версию.
  7. Выберите версию Киберпанели.

#### Шаг №9: Установите пароль для CyberPanel
  Пароль по умолчанию для установки Cyberpanel — 1234567. Как видите, он довольно слабый. CyberPanel позволяет вам установить более надежный пароль для вашей установки.
  Для этого введите «s» и дважды введите надежный пароль.
  8 Ручная установка пароля Киберпанели

#### Шаг № 10. Установите PHP-расширение CyberPanel Memcached.
  Memcached — одно из самых популярных расширений PHP. Это высокопроизводительная система кэширования с распределенной памятью, которая ускоряет работу веб-приложений за счет снижения нагрузки на базу данных.
  Его можно использовать для кэширования объектов, баз данных и страниц. RedSwitches рекомендует установить это расширение во время установки CyberPanel.
  9. Установите Memcached

#### Шаг № 11: Установите PHP-расширение CyberPanel Redis
  Redis — еще один мощный инструмент для оптимизации производительности веб-сайта.
  Расширение CyberPanel Redis позволяет разработчикам хранить и извлекать данные из Redis, хранилища структур данных в памяти. Расширение предлагает множество ключевых преимуществ, включая улучшенную масштабируемость, меньшую задержку и лучшее использование ресурсов. RedSwitches рекомендует установить это расширение на сервер во время установки CyberPanel.
  10. Установите Редис

#### Шаг № 12: Завершите установку
  Завершите установку, выполнив остальные шаги и завершите процесс.
  После этого войдите в CyberPanel из вашего веб-браузера. Для этого откройте новую вкладку и введите IP-адрес вашего сервера, а затем номер порта 8090.
  11 Завершите установку Cyberpanel.
  Разрешить порты CyberPanel через брандмауэр
  После установки. Следующий шаг — разрешить порты CyberPanel через брандмауэр.
  Важно убедиться, что правильные порты внесены в белый список брандмауэра сервера. По умолчанию CyberPanel работает через порты 8090 (HTTP) и 8091 (HTTPS). Настоятельно рекомендуется открыть эти порты (внести их в белый список), чтобы обеспечить безопасный доступ пользователей к панели управления.
  #Как только эти порты будут открыты, пользователи смогут получить доступ к панели управления CyberPanel из любого веб-браузера.
  12 Разрешить порты Cybpernel
  > ВАЖНО : Если ваш сервер находится за аппаратным брандмауэром RedSwitches, вам может потребоваться настроить его по-другому, чтобы открыть необходимые порты. Мы настоятельно рекомендуем связаться с нашей поддержкой через тикет, электронную почту или чат.
  Доступ к Киберпанели
  Получив доступ к странице входа в CyberPanel, вы можете использовать учетные данные по умолчанию для входа в систему.
  Сначала введите «admin» в качестве имени пользователя, а затем введите пароль, который вы ввели в процессе установки.

#### 13 Доступ к Киберпанели
  После входа в систему вы можете начать настройку и управление средой веб-хостинга через панель управления CyberPanel.
  Начните с создания учетной записи, настройки DNS-записей и установки приложений.
  14 Создать новый сайт
  Доступ к OpenLiteSpeed
  
#### После успешной установки CyberPanel на свой сервер Ubuntu 22.04 LTS вы можете получить доступ к веб-серверу OpenLiteSpeed ​​по следующему URL-адресу: #http://ip-адрес вашего сервера:7080

  ```bash
    #Если вы не уверены в пароле, выполните следующую команду, чтобы сбросить пароль панели OpenLiteSpeed:
     #/usr/local/lsws/admin/misc/admpass.sh
  ```


## 🟢 5. Aapanel

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 6. Froxlor

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 7. Virtualmin
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 🟢 8. Zpanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 9. FastPanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 10. Control Web Panel

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 11. DirectAdmin

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 12. Solid CP

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 13. MediaCP

  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```


## 🟢 14. Vesta CP

🌐 URL: [Vesta CP Install](https://vestacp.com/install/)

  ### DEFAULT INSTALL SETTINGS:
  
  ```bash
    apt update && apt install -y wget curl
    mkdir -p /temp && cd /temp ;
    
    # Download installation script
    curl -O http://vestacp.com/pub/vst-install.sh && chmod +x vst-install.sh && bash vst-install.sh
  ```

  ### ADVANCED INSTALL SETTINGS:
  
  ```bash
    apt update && apt install -y wget curl;
    mkdir -p /temp && cd /temp ;
    
    read -p "Enter hostname: " WEBPanelHostname
    read -p "Enter Admin Email: " WEBPanelEmail
    read -p "Enter Admin Password: " WEBPanelPassword
    
    bash <(curl http://vestacp.com/pub/vst-install.sh || wget -O - http://vestacp.com/pub/vst-install.sh) \
    --nginx yes --apache yes --phpfpm no --named yes --remi yes \
    --vsftpd no --proftpd yes \
    --iptables yes --fail2ban yes \
    --quota yes \
    --exim yes --dovecot yes --spamassassin yes --clamav yes \
    --softaculous yes \
    --mysql yes --postgresql yes \
    --hostname ${WEBPanelHostname} --email ${WEBPanelEmail} --password ${WEBPanelPassword}
    
    # ************
    # URL: – https://your-host:8443
    #
    # END
  ```


## 🟢 13. webmin

🌐 URL: [webmin Install](https://webmin.com/download/)

  ### Debian and derivatives
  
  ```bash
    curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh
    sh setup-repos.sh
    apt-get install webmin --install-recommends
    apt-get install --install-recommends ./webmin-current.deb
  ```

  ### RHEL and derivatives
  
  ```bash
    curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh
    sh setup-repos.sh
    dnf install webmin
    dnf install ./webmin-current.rpm
  ```

  ### Solaris
  
  ```bash
    # The root user be switched from a role account to a normal account to logins to work
    rolemod -K type=normal root
    # Uncompress
    gunzip webmin-current.pkg.gz
    # Install
    pkgadd -d webmin-current.pkg
  ```

  ### FreeBSD and any other Linux installation from source
  
  ```bash
    # Change directory
    cd /tmp
    # Uncompress
    gunzip webmin-current.tar.gz
    tar xf webmin-current.tar.gz
    cd webmin-current
    # Install
    ./setup.sh /usr/local/webmin
  ```


_____________________________________________________________
_____________________________________________________________







# ❌❌NON-Free WEBPanels for server management
************************************
✅✳️❎⚠️❌⭕️

## 1. cPanel
  ```bash
      sh <(curl install.sh || wget -O - install.sh)
      #
      # ************
      # URL: – https://your-host:80
      #
      # ****** END
  ```

## 2. Plesk
   ```
   sh <(curl https://autoinstall.plesk.com/one-click-installer || wget -O - https://autoinstall.plesk.com/one-click-installer)

   # _________
   # URL: – https://your-host:8443

   # END
   ```

