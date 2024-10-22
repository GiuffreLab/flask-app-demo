# import necessary libraries from Flask and app instance
from flask import Blueprint, render_template, request, current_app

# Define a Blueprint for the views
main = Blueprint('main', __name__)

# Middleware to log every request before it is processed
@main.before_app_request
def log_request_info():
    current_app.logger.info(
        "Request received: Method: %s, Path: %s, IP: %s",
        request.method,
        request.path,
        request.remote_addr,
    )

# Home route
@main.route("/")
def home():
    container_hostname = current_app.config.get('container_hostname', 'Unknown')
    environment = current_app.config.get('environment', 'Unknown Environment')
    return render_template("index.html", container_hostname=container_hostname, environment=environment)
