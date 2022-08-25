#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

sudo sed -i "50i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default

sudo service nginx restart