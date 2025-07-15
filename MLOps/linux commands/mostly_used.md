## 📦 Basic System Maintenance

```bash
sudo apt update -y            # Update package lists
sudo apt upgrade              # Upgrade packages
sudo apt install <pkgname>    # Install package
sudo apt remove <pkgname>     # Remove package
```

## Download Docker installation script
```bash
curl -fsSL https://get.docker.com -o get-docker.sh

# Run the installation script
sudo sh get-docker.sh

# Add current user to docker group
sudo usermod -aG docker ubuntu

# Activate the docker group without logout/login
newgrp docker
```

## ✅ Check Docker Status
```bash
docker ps    # Check if Docker is running
```


## 💾 Check EC2 Disk Space
```bash

df -h    # Check available disk space

lsblk # list blockstorage

```

## 🧹 Clean Docker From EC2
```bash
# Stop all running containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove dangling images
docker image prune -f

# Remove all unused images, networks, and volumes
docker system prune -a -f --volumes
```


## Keep GitHub Actions Runner Running

```bash
cd actions-runner

# Install the runner as a service
sudo ./svc.sh install

# Start the runner service
sudo ./svc.sh start

```

## Test from EC2 if container working

```bash 
curl http://localhost:5000

```


## Working directory on EC2 after CI/CD pipeline
```markdown
When you use:
- name: Checkout
  uses: actions/checkout@v3

Always checkout the repo to:
<runner-root>/_work/<repo-name>/<repo-name>/

Find your runner root:
ls /home/ubuntu/actions-runner/_work/
it look inside work folder to see if their is anything in it.and then add that path to CD(continious-deployment) just before executing docker run commands
```

## TO check if container is working or not
```bash
docker ps -a  #see all container and their status
docker logs fastapi_service  #check logs for fast api container
docker start -ai fastapi_service #rerun the container

```

## Mostly Used Linux Commands
```bash
cd <directory>  #Change directory 
mkdir <new_folder>   #Make a new directory
pwd  #Print working directory

ls        #  list files
ls -l     # detailed list
ls -a     # show hidden files

touch filename.txt  #Create an empty file
cat filename.txt  #View file contents
rm <filename.txt>  # Remove a file
rm -r <directory_name>  #Remove a directory and its contents

# Move or rename files and directories
mv <old_name> <new_name>
mv <file.txt> </path/to/destination/>

```
