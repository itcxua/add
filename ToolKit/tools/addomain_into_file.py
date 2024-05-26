#!/usr/bin/python3
import sys
import re
import os

os.system("clear")
file_path = input("Enter file path: ")
path_sites_available = "/etc/nginx/sites-available/"
path_sites_enabled = "/etc/nginx/sites-enabled/"
root_path = "/var/www/"
docker_www_path = "/var/www/"

conf_content = """
### Configuration ###
    server {{
        listen 80;
        listen [::]:80;
        listen 443;
        listen [::]:443;
        server_name www.{0} {0};
        root /var/www/{0};
        index index.php index.html index.htm index.nginx-debian.html;

        proxy_connect_timeout 3600;
        proxy_send_timeout 3600;
        proxy_read_timeout 3600;
        send_timeout 3600;
        client_max_body_size 100M;

        location / {{
            try_files $uri $uri/ /index.php$is_args$args;
        }}

        location ~ "^\/([a-z0-9]{{28,32}})\.html" {{
            add_header Content-Type text/plain;
            return 200 $1;
        }}

        location ~* \\.php$  {{
            try_files $uri $uri/ /index.php last;
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
            fastcgi_index index.php;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param REMOTE_ADDR $remote_addr;
            fastcgi_param HTTP_X_FORWARDED_FOR $http_x_forwarded_for;
            fastcgi_param HTTP_X_REAL_IP $http_x_real_ip;
            fastcgi_param HTTP_CF_CONNECTING_IP $http_cf_connecting_ip;
            fastcgi_intercept_errors off;
            fastcgi_buffer_size 16k;
            fastcgi_buffers 4 16k;
            fastcgi_read_timeout 3600;

        }}

        location ~* \\.(jpg|jpeg|png|gif|ico|css|js|mp4|svg|woff|woff2|ttf)$ {{
            expires 365d;
        }}

        location ~* /(?:uploads|files)/.*.php$ {{
            deny all;
        }}

        location ~* /*.sql {{
            deny all;
        }}

        location ~* /.git/* {{
            deny all;
        }}
        location  ^~ /wp-cron.php {{
               allow 127.0.0.1;
        }}

        location ~ /\\.ht {{
                deny all;
        }}

        location = /xmlrpc.php {{
            deny all;
        }}

        location ~ /\\. {{
            deny all;
        }}
    }}


"""
html_content = """
<!DOCTYPE html>
<html>
<body>

<h1 style="color:black;">{0} OK!</h1>

</body>
</html>
"""


fp = open(file_path, 'r')
location_content = fp.readlines()
if not location_content:
    # string is absent in the text file
    print("This is a first time location.conf used")
else:
    for lines in location_content:
        location_regexp = re.compile(r'\w.*\b$')
        found = location_regexp.search(lines)
        print("\n=========================  " + found.group() + "  =========================")

        domain_name = found.group()
#        with open(path_sites_available + domain_name + ".conf", "w+") as fp:
#            fp.write(conf_content.format(domain_name, root_path, domain_name, proxy_server))
        fp = open(path_sites_available + domain_name + ".conf", "w+")
        fp.write(conf_content.format(domain_name))
        if os.path.isfile(path_sites_enabled + domain_name + ".conf"):
            print("\nNote: Config " + path_sites_enabled + domain_name + ".conf" + " exists")
        else:
            os.system("cd " + path_sites_enabled + "; ln -s ../sites-available/" + domain_name + ".conf")
        if os.path.isfile(docker_www_path + domain_name + "/index.html"):
            print("\nNote: Folder " + docker_www_path + domain_name + " already exists \n")
        else:
            os.system("mkdir " + docker_www_path + domain_name)
            fp = open(docker_www_path + domain_name + "/index.html", "w+")
            fp.write(html_content.format(domain_name))


        os.system("chown www-data:www-data -R " + docker_www_path + domain_name)
        os.system("chmod 775 -R " + docker_www_path + domain_name)
# os.system("docker service update dt_web --force")
os.system("nginx -s reload")
# This creates a symbolic link on python in tmp directory
print("\nScript has done\n\n===========================================================================")
