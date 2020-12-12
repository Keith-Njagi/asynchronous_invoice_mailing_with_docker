# Pull from this image
FROM nginx

# Remove nginx default config file and replace it with our config file
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/