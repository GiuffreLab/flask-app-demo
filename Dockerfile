FROM python:alpine

# Set up the working directory
WORKDIR /app

# Create a non-root user with UID 1000
RUN adduser -D -u 1000 webapp_user

# Copy requirements.txt if there are any dependencies
COPY requirements.txt requirements.txt

# Install dependencies if there are any
RUN pip install -r requirements.txt || true

# Copy the Flask app to the container
COPY . .

# Set the Flask environment variable to development for debugging
ENV FLASK_ENV=development

# Switch to the new user
USER webapp_user

# Run the Flask app
CMD [ "python", "app.py" ]
