# Dockerfile
FROM ubuntu:22.04

RUN sudo apt-get update && sudo apt-get install gnupg2 -y
# Install SSH client
RUN apt-get update && apt-get install -y openssh-client
RUN apt-get update && apt-get install -y python3 python3-pip

# Other setup steps...