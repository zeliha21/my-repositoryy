#!/bin/bash -x

# update the system and install apache
yum update -y
yum install httpd -y

# change to the correct directory and download web content
cd /var/www/html
FOLDER=https://raw.gicontent.com/zeliha21/my-repositoryy/main/101-kittens-carousel-static-website-ec2/static-webthubuser
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg

# start and enable httpd
systemctl start httpd
systemctl enable httpd