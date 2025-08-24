```bash
# Build an image from Dockerfile
docker build -t myimage:latest .

# List all images
docker images

# Tag an image
docker tag myimage username/myimage:tag

# Remove an image
docker rmi image_id_or_name
```
### Container
```bash
# Run a container
docker run -d -p 5000:5000 --name mycontainer myimage

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a running container
docker stop container_id_or_name

# Start a stopped container
docker start container_id_or_name

# Remove a container
docker rm container_id_or_name

# View logs
docker logs container_id_or_name

# List volumes
docker volume ls

```

### Pushing to docker hub
```bash
docker login

# Tag image for Docker Hub
docker tag localimage username/repo:tag

# Push to Docker Hub
docker push username/repo:tag

# Pull from Docker Hub
docker pull username/repo:tag


```
### Clean up
```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune

# Remove all unused volumes
docker volume prune

# Remove everything not in use
docker system prune -a

```

### Build-tag-push
```bash
docker build -t myimage:latest .
docker tag myimage username/myimage:tag
docker push username/repo:tag

```

### .Env in docker

```bash
docker run --env-file .env <image-name>
docker run -p 5000:5000 --env-file .env vehicle

```

### For 2 Docker files(streamlit+fastapi) docker-compose.yaml
```bash
docker compose build  # Builds all images defined in docker-compose.yml.
docker compose up --build #Build images and start containers
docker compose up -d  #Runs containers in the background.
docker compose stop   #Stop conatianer
docker compose down    # Stops and removes everything created by docker-compose up.
docker compose pull #Pull new images from registry
docker compose ps #Check status
docker compose restart
docker system df  #To check how much disk space your containers and images are using, run

docker compose down --volumes --rmi all   #remove every docker compose conter completely

# Install docker compose on AWS EC2
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
#Verify
docker compose version

```
## Docker-compose test in Local
```bash
docker compose up
docker compose up -d  #run in background

docker compose up <fastapi>  #run specific container
docker compose logs <fastapi_service> #to check any issue in any container

http://localhost:8501  # to test streamlit
http://localhost:8000   # to test fast api

docker compose down #after testing close the container just close container not remove
docker compose down --volumes --rmi all
 #remove container space and image also


```


## How to restore deleted file
```bash
# 1️⃣ View the commit history that included the file
git log -- src/component/data_ingestion.py

# 2️⃣ Inspect a specific commit to find the exact path
git ls-tree -r --name-only <commit-hash>

# 3️⃣ Restore the file from that commit
git checkout <commit-hash> -- src/component/data_ingestion.py

```

## How to switch back to previous commit
```bash
# ✅ Method 1: Temporary rollback (safe)
# This switches to a previous commit without changing branch history.
git switch --detach <commit-hash>

# If you want to keep working from this state,
# create a new branch pointing to this commit:
git checkout -b my-rollback-branch

# ------------------------------------------------------

# ✅ Method 2: Permanent reset (rewrites history!)
# This resets your current branch pointer to an old commit,
# discards any newer commits, and updates the remote.
git reset --hard <commit-hash>

# Force push is required because you’re rewriting branch history.
git push origin main --force

```