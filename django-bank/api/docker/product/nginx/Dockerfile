FROM docker.io/nginx:1.29.1-alpine3.22-slim

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/nginx/conf.d/default.conf