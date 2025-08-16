FROM nginx:latest

COPY templates /etc/nginx/templates

ENV NGINX_HOST=0.0.0.0
ENV NGINX_PORT=80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]