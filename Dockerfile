
FROM ros:humble

RUN apt update && apt install -y \
    python3-pip \
    git

WORKDIR /root/ws
