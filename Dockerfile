FROM ubuntu:20.04
MAINTAINER Oleksandr Ponomarov <oleksandr@appsilon.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN set -eux && apt-get update -qq && apt-get install -y \
    curl            \
    python3-pip     \
 && rm -rf /var/lib/apt/lists/* $HOME/.cache

ARG ansible_version="2.11.4"
ENV ANSIBLE_VERSION ${ansible_version}

RUN pip install ansible-core==${ANSIBLE_VERSION}

COPY . /etc/ansible/roles/ansible-role
WORKDIR /etc/ansible/roles/ansible-role

RUN ansible-playbook -i localhost, tests/test.yml --connection=local
