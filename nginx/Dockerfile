FROM nginx:1.14

ADD app/static /usr/share/nginx/html
ADD conf/server.template /etc/nginx/conf.d/
ADD docker-entrypoint.sh /
# RUN chmod 777 /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]