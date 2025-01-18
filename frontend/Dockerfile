# frontend/Dockerfile
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Serve the application
EXPOSE 3000
CMD ["npx", "serve", "-s", "build"]
