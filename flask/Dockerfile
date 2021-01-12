FROM ubuntu:20.04

LABEL maintainer="stephan.semerad@gmail.com"
LABEL version="0.1"
LABEL description="pdf-rendering-service"
RUN apt update


COPY start.sh /start.sh
CMD ["./start.sh"]

RUN apt install -y nginx php-fpm supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean
    

EXPOSE 80 443
