#!/bin/bash

# install or update the AWS CLI

# (optional) get gpg commands
yum install -y gpg curl unzip zip

# Download installation file
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# unzip installer
unzip awscliv2.zip

# Run install/update program
 ./aws/install

 ./aws/install --update

# installation confirmation
  /usr/local/bin/aws --version
  #set variable for path
  export PATH=$PATH:/usr/local/bin/

# aws credentials
aws configure

#aws ec2 describe-instances --region us-east-1 | grep "PrivateIpAddress"
#aws ec2 describe-instances --region us-west-1 | grep "PrivateIpAddress"
#aws ec2 describe-instances --region us-south-1 | grep "PrivateIpAddress"
#aws ec2 describe-instances --region us-north-1 | grep "PrivateIpAddress"

echo   export PATH=$PATH:/usr/local/bin/ >>~/.bashrc

echo   export PATH=$PATH:/usr/local/bin/ >>/home/admin/.bashrc

#filter out to ip addresses
git config --global credential.helper store

# erase ipad.json
rm ipad.json

#git clone https://gitlab.com/discord-fiends/roy-rogers.git
aws ec2 run-instances --image-id ami-04a32162efe87cb4c --count 1 --instance-type t2.micro --key-name JESSEANDREWKEY --security-group-ids >>ipad.json
cat ipad.json | grep "PrivateIpAddress"

# check status
aws ec2 describe-instances --region us-west-2 | grep "PrivateIpAddress"
