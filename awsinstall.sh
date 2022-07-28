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
