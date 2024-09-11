# Dockerfile
FROM ubuntu:22.04

RUN sudo apt-get update && sudo apt-get install gnupg2 -y
# Install SSH client
RUN apt-get update && apt-get install -y openssh-client
RUN apt-get update && apt-get install -y python3 python3-pip

# Other setup steps...
# Install Docker CLI tools
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable"

RUN apt-get update && apt-get install -y docker-ce-cli
        