# aws credentials
aws configure

aws ec2 describe-instances --region us-east-1 | grep "PrivateIpAddress"
aws ec2 describe-instances --region us-west-1 | grep "PrivateIpAddress"
aws ec2 describe-instances --region us-east-2 | grep "PrivateIpAddress"
aws ec2 describe-instances --region us-west-2 | grep "PrivateIpAddress"
