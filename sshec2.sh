#!/bin/bash
# this is redhat ami
AMI=ami-0686851c4e7b1a8e1
USER=centos
# this is ubuntu
# AMI=ami-04a32162efe87cb4c
# USER=ubuntu
# remove ipad file
rm ipad.json

# create new instance
aws ec2 run-instances --image-id $AMI --count 1 --instance-type t2.micro --key-name JESSEANDREWKEY --security-group-ids >>ipad.json

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
echo "Please wait for the vm to start before it can connect this will take 60 seconds"
sleep 50
echo ssh -i $1 $USER@$PUBLICIP
scp -o StrictHostKeyChecking=no -i $1 $2 $USER@$PUBLICIP:~/Provision.sh
ssh -o StrictHostKeyChecking=no -i $1 $USER@$PUBLICIP "sudo bash Provision.sh"
echo "hey were trying to connect but its going to take a little more time then expected"
sleep 20
ssh -i $1  $USER@$PUBLICIP
