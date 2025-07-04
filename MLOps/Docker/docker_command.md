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