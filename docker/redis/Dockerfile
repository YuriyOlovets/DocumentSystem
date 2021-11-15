FROM redis:latest

COPY ./config/redis.conf /usr/local/etc/redis/redis.conf

WORKDIR /data

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]