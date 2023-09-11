# Use NodeJS image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY ui ./

# Install frontend dependencies
RUN npm install

# Build the frontend
RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]
