#!/bin/bash
# update system

sudo apt-get update -y

# upgrade system

sudo apt-get upgrade -y

# install nginx

sudo apt-get install nginx -y

# install nodejs

sudo apt-get install nodejs -y

# install npm

sudo apt-get install npm -y

# install pm2

sudo npm install pm2@latest -g

# install python properties

sudo apt-get install python-software-properties -y

# install specific nodejs version

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get install nodejs -y

# set up reverse proxy for nginx
sudo systemctl start nginx
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
sudo systemctl reload-or-restart nginx
