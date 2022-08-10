#!/bin/bash
# this is centos 7 ami
AMI=ami-0686851c4e7b1a8e1
USER=centos

# this is ubuntu
# AMI=ami-04a32162efe87cb4c
# USER=ubuntu

# instance type
# typeinstance=t2.micro

typeinstance=t2.2xlarge

# typeinstance=t3.medium

# personal key
# privkey=ANDREWJESSEKEY.pem

# remove ipad file
rm ipad.json

# create new instance
aws ec2 run-instances --image-id $AMI --count 1 --instance-type $typeinstance --key-name JESSEANDREWKEY --security-group-ids >>ipad.json

# find instance ID
echo "hi were getting your new instance id"
cat ipad.json | jq -r  '.Instances[].InstanceId'
export INSTANCEID=$(cat ipad.json | jq -r '.Instances[].InstanceId')
#aws ec2 describe-instances --region us-west-2 | grep "Instance"
#thisisacomment
export PUBLICIP=""
# print message
echo "please wait a minute while we get the ip address"
while [ -z "$PUBLICIP" ]
do
	echo "Press [CTRL+C] to stop.."
	sleep 20
	source getpublicipaws.sh $INSTANCEID
echo ip: $PUBLICIP
done
echo "Please wait for the vm to start before it can connect this will take 80 seconds"
sleep 70
echo ssh -i $1 $USER@$PUBLICIP
scp -o StrictHostKeyChecking=no -i $1 $2 $USER@$PUBLICIP:~/Provision.sh
ssh -o StrictHostKeyChecking=no -i $1 $USER@$PUBLICIP "sudo bash Provision.sh"
ssh -o StrictHostKeyChecking=no -i $1  $USER@$PUBLICIP

