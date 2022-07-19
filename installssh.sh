#!/bin/s

# update centOS
yum update -y

# installing ssh
yum –y install openssh-server openssh-clients

systemctl start sshd

# continue install ssh
systemctl status sshd -y

systemctl stop sshd -y

systemctl enable sshd -y

# uncomment root login and disable (put no instead of yes)
# vim /etc/ssh/sshd_config
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# restart sshd
service sshd restart -y
