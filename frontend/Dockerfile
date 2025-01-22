# Use the official Node.js image for building the React app
FROM node:16 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the entire application source code
COPY . .

# Build the React app for production
RUN npm run build

# Use Nginx to serve the production build
FROM nginx:alpine

# Copy the build folder to the Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
