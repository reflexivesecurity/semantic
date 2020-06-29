FROM ubuntu:19.10

RUN apt update

RUN apt install git -y

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["sh","/entrypoint.sh"]