# Microservices, Containers, and Docker - Summary

## Key Definitions and Concepts

- **Microservices Architecture**: An approach where applications are built as collections of small, autonomous services that communicate via lightweight APIs, each owning its data and business logic

- **Container**: Lightweight, portable units that package applications with all dependencies (code, runtime, libraries) and share the host OS kernel

- **Docker**: Leading containerization platform with client-server architecture consisting of daemon, client, registry, and Docker objects (images, containers, volumes, networks)

- **Dockerfile**: Text script containing instructions (FROM, RUN, COPY, CMD, EXPOSE, ENV, WORKDIR) to build Docker images layer by layer

- **Docker Compose**: Tool for defining and running multi-container applications using YAML configuration files

## Important Formulas and Concepts

- Docker image layering: Each instruction creates a read-only layer; containers add a writable layer on top
- Container isolation: Namespaces and cgroups provide process isolation and resource control
- Service discovery: Docker's embedded DNS resolves container names to IP addresses in user-defined networks

## Key Points

- Microservices enable independent deployment, scaling, and technology choices per service
- Containers start in seconds and use significantly fewer resources than virtual machines
- Docker uses a union filesystem (like OverlayFS) for efficient storage
- Multi-stage builds reduce final image size by copying only necessary artifacts
- Docker Compose defines service dependencies, networks, and volumes in a single file
- Health checks in Docker Compose ensure services start in the correct order
- Microservices must handle partial failures gracefully using circuit breakers and timeouts
- Each microservice owns its database, avoiding shared database schemas
- Volumes persist data beyond container lifecycle; bind mounts sync host files in real-time

## Common Mistakes to Avoid

- Running containers with root user instead of specifying USER instruction in Dockerfile
- Not exposing ports correctly in both EXPOSE and docker run -p flag
- Creating overly large images by including unnecessary build dependencies
- Not using .dockerignore to exclude files from build context
- Starting services in containers before dependencies are ready (use depends_on with health checks)
- Leaving debug ports exposed in production containers
- Not cleaning up unused images and containers, leading to disk space issues

## Revision Tips

1. Practice writing Dockerfiles from scratch for different language runtimes (Node.js, Python, Java)
2. Run through the complete workflow: build image → run container → check logs → exec into container → stop and remove
3. Create a multi-container application using Docker Compose to understand service dependencies and networking
4. Memorize the sequence of Dockerfile instructions and understand layer caching for optimization
5. Review common docker commands and their flags until you can recall them from memory
6. Understand the difference between bridge, host, and overlay network drivers