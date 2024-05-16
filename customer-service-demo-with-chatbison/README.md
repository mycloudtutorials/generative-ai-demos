# Simple Customer Service Agent Demo - Generative AI Application - Hands On Coding
## Built Using Google Vertex AI, Langchain, Python, Docker
## Models used:
    Chat-Bison

## Introduction
This video shoes how to build a simple customer service agent that helps customers with item return.
The model is provided context, so it asks questions to the customers if the item was purchased within last 15 days and it's unused.
It makes the decision based on the Customer's response to those questions.

The video also shows how to enhance user experience by streaming responses from the Large Language Model (LLMs).

## What will you learn:
  - How to create key for Service Account in Google Cloud Platform
  - Build Docker Image with the python packages needed
  - How to mount the key on Docker image in runtime, so you don't accidentally share your key file
  - Build the Streamlit application with Langchain, Python and Google Cloud AI Platform SDK

### Docker Commands:

  Build Docker Image:
  `docker build -t simple-customer-service-demo .`

  Run ADMIN application:
  `docker run -v <FOLDER_PATH_FOR_KEY_FILE>:/root/key -p 8083:8083 -it simple-customer-service-demo`


#### Note: The docker volume mount is only needed in local. If you are running the container in CloudRun, GKE, ECS, or EKS, the iam role is used. Please check the approprite cloud provider's documentation.


## Youtube
I have created a Youtube video for this tutorials with step-by-step hands-on coding.

[![Simple Customer Service Agent - Generative AI Application With Chat Model](https://i9.ytimg.com/vi/McGWCwSCjd8/mqdefault.jpg?v=664644ff&sqp=CPCJmbIG&rs=AOn4CLDT5WJAKuPIaOjQfMn0sbKa-ZKduQ)](https://www.youtube.com/watch?v=McGWCwSCjd8)

