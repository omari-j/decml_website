FROM python:3.12.2

# Set the working direct directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
RUN requirements.txt /app/

# Install any dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI and jq
RUN pip install awscli
RUN apt-get update && apt-get install - jq

# Copy the current directory contents into a the container at /app
COPY . /app/

# Copy entrypoint script
COPY entrypoint.sh /app/

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
