#!/bin/bash

# echo this is the first parameter: $1
# echo this is the second parameter: $2
# echo this is the third parameter: $3

# create variable function to cat out instance id
idinstance=$(cat ipad.json | jq -r '.Instances[].InstanceId')

# print instance id
echo $idinstance

# use variable (instance id) terminate instance
aws ec2 terminate-instances --instance-ids $idinstance
