FROM ubuntu:19.10
ENV LC_CTYPE C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
COPY to_share/* .
WORKDIR /shr
RUN dpkg --add-architecture i386 && \

## Core linux updating/cli utility
apt-get update && \
apt-get install -y build-essential jq strace ltrace curl wget rubygems gcc dnsutils netcat gcc-multilib net-tools vim gdb gdb-multiarch python3 python3-pip python3-dev libssl-dev libffi-dev wget git make procps libpcre3-dev libdb-dev libxt-dev libxaw7-dev python-pip libc6:i386 libncurses5:i386 libstdc++6:i386 && \
## Hacky add-ons
# apt-gets
apt-get install nmap -y && \
apt-get install ncat -y && \
apt-get install stegohide -y && \
apt-get install tmux -y && \
# git cloning
cd /root/tools && \
git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh && cd .. && \
git clone https://github.com/JonathanSalwan/ROPgadget && \
# pipping
pip3 install pwntools requests keystone-engine unicorn capstone ropper && \
# gemming
gem install one_gadget