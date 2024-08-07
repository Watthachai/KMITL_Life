# Use the official MySQL image from the Docker Hub
FROM mysql:5.7

# Set environment variables using the correct format
ENV MYSQL_ROOT_PASSWORD=db4dev$
ENV MYSQL_DATABASE=users
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=db4dev$

# Copy the initialization script to the Docker image
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306