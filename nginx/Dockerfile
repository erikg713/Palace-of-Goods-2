# Use the official Nginx image
FROM nginx:alpine

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the React build output to the Nginx web directory
COPY ../frontend/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
