# Kubernetes
In this repository I do learn Kubernetes. Sections I am going to follow,

> [Kubectl](#Kubectl)  

### Vitrualization technology
* Docker is one implementation of container based vritualization technologies.
* Pre-Virtualization world,
 - Huge cost on purchasing physical machine
 - Configure servers may take time
 - Hard to migrate
* Hypervisor-based Virtualization
 - Hypervisor-providers(VMware, VirtualBox)
 - Now, AWS and MS Azure
 - Cost efficient - no upfront committment
 - Easy to scale
 - Limitations: Kernal resource duplications(all OSs are build on single hypervisor), Application portability issue\
 - Virtualization happens hardware level
 - OSs share kernal resources on base server
* Container Virtualization
 - Instead of a Hypervisor, Virtualization happens in Container Engine
 - Virtualization happens at the operating system level
 - Cost efficient
 - Fast Deployment
 - Guranteed Portability

### Runtime Isolation - A Benifit of Container Virtualization
* Isolating runtime environment
* Running two different applications in two different containers with the different JRE versions.

### Kubectl
* Kubectl provides access to nearly every Kubernetes.
* Primary command line access tool

###Docker-Commands
- docker run <arguments> sleep 1000 - make conatiner to run 1000 seconds and then exit
- docker-machine ls outputs docker-deamon IP
- docker history <image:tag> lists out image layers
- docker commit <container id> <repositoryname:tag> would save the changes we made to the docker container's file system to a new image.
- list out all running processes in the container
    * docker exec -it <container id> bash - log into container
    * pwd - prints working directory
    * cd /home/<username> - enter to home directory of the user
    * ps axu - displays all the running processes in the container
- docker run -d <container id> --link <container name> can link container to another container
    * after linking it can be tested by log into container
    * commands, 
        - more /etc/hosts - open up host file and link is there
        - ping to link name
        - docker inspect <container id> | grep IP


###Chain Run Instructions
- Each RUN commands will execute the command on the top of writable layer of the container, then commit the container as a new image.
- The new image is used for the next step in the Dockerfile. So each RUN instruction will create a new image layer.
- It is recommended to chain the RUN instructions in the Dockerfile to reduce the number of image layers it creates. 

###Docker-Compose
- docker-compose up command will not build the image if image is already exists.
- docker-compose build command will do the job
- other docker-compose commands are, up, ps, logs, logs <Container ID>, stop, rm
