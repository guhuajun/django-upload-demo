FROM nginx:1.14

COPY app/dist/ /usr/share/nginx/html/dist/
COPY app/index_prod.html /usr/share/nginx/html/index.html
COPY app/favicon.ico /usr/share/nginx/html/favicon.ico

ADD conf/server.template /etc/nginx/conf.d/
ADD docker-entrypoint.sh /
# RUN chmod 777 /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]