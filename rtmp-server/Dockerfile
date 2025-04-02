FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y nginx libnginx-mod-rtmp && \
    rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
