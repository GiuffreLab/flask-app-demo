# import necessary libraries
from flask import Flask
import logging
import os
import socket
from views import main  # Import the Blueprint from views

# create an app instance
app = Flask(__name__)

# Configure the logging format to include timestamp, log level, and message
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Determine the environment and hostname
if os.getenv('KUBERNETES_SERVICE_HOST'):
    # If the KUBERNETES_SERVICE_HOST variable is set, we are running in Kubernetes
    container_hostname = os.getenv('HOSTNAME', 'Unknown Pod')
    environment = 'Kubernetes'
elif os.getenv('HOSTNAME'):
    # If HOSTNAME is set but we are not in Kubernetes, we are likely in Docker
    container_hostname = os.getenv('HOSTNAME', 'Unknown Container')
    environment = 'Docker'
else:
    # Otherwise, we are running locally
    container_hostname = 'LocalHost-' + socket.gethostname()
    environment = 'Local'

# Set the hostname and environment in app config
app.config['container_hostname'] = container_hostname
app.config['environment'] = environment

# Register the Blueprint from views
app.register_blueprint(main)

# on running python app.py
if __name__ == "__main__":
    # read the port from an environment variable
    port = int(os.getenv("PORT", 8080))
    # run the flask app
    app.run(host="0.0.0.0", port=port, debug=False)
