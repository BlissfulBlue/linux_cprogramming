#!/bin/bash
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo systemctl reload firewalld

sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix



curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash


ip4=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
#sudo EXTERNAL_URL="https://$ip4" yum install -y gitlab-ee
sudo yum install -y gitlab-ee
cat /etc/gitlab/initial_root_password
publicip=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
echo "USERNAME IS root"
cat /etc/gitlab/initial_root_password
echo "http://$publicip"
