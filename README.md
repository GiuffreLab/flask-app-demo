# Flask Web Application Documentation

## Overview
This Flask web application serves a simple, visually appealing web page that displays environment-specific information. The app is designed to be easily run locally as a Python application, as well as in containerized environments like Docker and Kubernetes. The primary focus is to demonstrate different configurations and environments through the user interface.

[GitHub Repo for Deploying in Kubernetes](https://github.com/GiuffreLab/kubernetes-kustomize-overlays)

## Running the Application as a Python Script

### Prerequisites
To run the application locally, you need:
- Python 3.9 or above
- `pip` (Python package manager)
- Dependencies specified in `requirements.txt` (such as Flask)

### Installation and Setup
1. **Clone the Repository**
   - Clone the repository containing the Flask app code:
     ```sh
     git clone <repository-url>
     cd <repository-directory>
     ```

2. **Install Dependencies**
   - Install the required Python packages using `pip`:
     ```sh
     pip install -r requirements.txt
     ```

3. **Run the Application**
   - Run the application using Python:
     ```sh
     python app.py
     ```
   - By default, the app runs on `http://127.0.0.1:8080`. You can access it by opening this URL in your web browser.

### Application Features
- **Home Page**: Displays a "Kubernetes Kustomization Test Page".
- **Container Hostname**: The app shows the hostname of the environment where it is running. If the app is run locally, it shows `LocalHost-<machine-name>`. If run in a container, it shows the container hostname.
- **Environment Type**: The application can detect and display the type of environment it is running in (e.g., Docker, Kubernetes, Local).
- **Logging**: The application has detailed logging configured. All incoming requests and relevant information are logged, which is useful for debugging and monitoring.

### Configuration
- **Port Configuration**: By default, the app runs on port `8080`. You can change the port by setting the `PORT` environment variable before running the application.
  ```sh
  export PORT=5000
  python app.py
  ```

## Running the Application in Docker (v1, v2, v3 Variations)

This Flask app has three visual variations (v1, v2, and v3) that are built into different Docker images. Each version provides a different aesthetic for the UI, demonstrating a simple way to differentiate application versions.

### Running the Docker Container
1. **Pull the Docker Image**
   - You can pull the specific version of the Docker image from Docker Hub using:
     ```sh
     docker pull giuffrelab/flask-web-app:<version>
     ```
     Replace `<version>` with `v1`, `v2`, or `v3` as needed.

2. **Run the Docker Container**
   - To run the container locally, use the following command:
     ```sh
     docker run -d -p 8080:8080 --name flask-web-app giuffrelab/flask-web-app:<version>
     ```
     Replace `<version>` with `v1`, `v2`, or `v3`.

   - The `-d` flag runs the container in detached mode, and `-p 8080:8080` maps port 8080 of the container to port 8080 on your local machine.

3. **Access the Application**
   - Open your browser and navigate to `http://localhost:8080` to view the running Flask app.

### Version Differences
- **v1**: The initial version of the application with the default "cyber" theme.
- **v2**: A slightly modified version of the UI, with color variations to differentiate it from v1.
- **v3**: Another visual variation that further tweaks the color scheme for demonstration purposes.

These visual variations are designed to help you understand how different versions of an application can be deployed and tested in different environments.

## Summary
This documentation provides instructions for running the Flask application both as a Python script and as a Docker container. The application is designed to demonstrate different configurations, such as environment-specific information and UI variations, making it an ideal candidate for testing containerized deployments.

