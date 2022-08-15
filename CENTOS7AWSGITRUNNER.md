## Pre-requisites
```1. clone a new vm. Go to hardware and proccessors and put in 2 sockets and 4 cores.```
```2. Type "ip a" in proxmox vm to get ip address for ssh (look for inet) and ssh in.```
```3. To ssh in, open powershell: ssh root@ip.address.here```
```4. Have AWS access key and secret access key ready.```
```5. Go to https://aws.amazon.com/ and create a rsa .pem keypair and download it.```

## Step 1:  Install git

```sudo yum install git```
```git --version```

## Step 2: Clone Repository [ERROR: Needs Username and Password]
```git clone https://gitlab.com/discord-fiends/roy-rogers.git```
```cd roy-rogers```

## Step 3: Download your tools
```ls -la```
```bash andrewtoolkit.sh```

## Step 4: Install AWS
```ls -la```
```bash step1awsinstall.sh```

## Step 5: Amazon Credentials
```ls -la```
```Have your access key and secret access key in a note pad and open```
```bash step2amazoncredentials.sh```
```Put in access keys.```
```(For our Centos 7 AMI), insert us-west-2 for region.``` 
```For output format/(file type), put in json```

## Step 6: Define AWS
```ls -la```
```bash step3defineaws.sh```

## Step 7: Create private key file
```Have your private key on notepad open and ready```
```touch KEYNAME.pem```
```nano KEYNAME.pem```
```Copy and paste entirety of private key inside file```
```Save and exit (ctrl o, enter, ctrl x).```

## Step 8: Launch instances (install gitlab server and runner)
```ls -la```
```bash step4all.sh KEYNAME.pem```
```Follow the gitlab website with http://ip.address.here echoed on the screen (underneath password). Username is root. Copy the password given to log in.```
```When logged in, create a blank project.```
```Type exit to continue. This will install gitlab runner on another insatnce.```
```NOTE: If the Provision files ever freeze for longer than 5 minutes on one line, ctrl C to cancel and try rerunning the script. (bash Provision.sh)```

## Step 9: Register Runner
```sudo gitlab-register runner```
```When inside the gitlab website, go to settings, CI/CD, and expand runners.```
```When prompted to insert url and registration token, copy and paste.```
```Press enter to skip description, skip tags, and skip optional maintenance notes.```
```Type in shell for executor. Refresh the page and expand runners to view active runner.```
