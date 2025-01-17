# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set environment variable to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Copy your configuration script
COPY 0-give_me_a_page /usr/local/bin/

# Make the script executable
RUN chmod +x /usr/local/bin/0-give_me_a_page

# Install Apache without starting it
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Run the configuration script to set up Apache
RUN /usr/local/bin/0-give_me_a_page

# Expose port 80 for Apache
EXPOSE 80

# Command to start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
