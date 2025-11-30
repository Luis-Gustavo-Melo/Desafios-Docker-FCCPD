FROM alpine:latest

RUN apk add --no-cache curl

COPY loop.sh /loop.sh

RUN chmod +x /loop.sh

CMD ["/loop.sh"]