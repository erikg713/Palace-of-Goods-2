# Use the official Node.js image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .

# Install dependencies
RUN npm install

# Copy the entire application code
COPY . .

# Build the React app for production
RUN npm run build

# Use Nginx to serve the built files
FROM nginx:alpine

# Copy the build folder to the Nginx directory
COPY --from=0 /app/build /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
