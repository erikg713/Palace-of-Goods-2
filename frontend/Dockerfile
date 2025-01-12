# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json /app/
RUN npm install

# Copy the rest of the frontend code into the container
COPY . /app/

# Build the React app
RUN npm run build

# Expose the default React port
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "start"]