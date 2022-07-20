#!/bin/s

# update centOS
yum update -y

# installing ssh
yum install -y openssh-server openssh-clients

systemctl start sshd

# continue install ssh
systemctl status sshd 

systemctl stop sshd 

systemctl enable sshd 

# uncomment root login and disable (put no instead of yes)
# vim /etc/ssh/sshd_config
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# restart sshd
service sshd restart 
