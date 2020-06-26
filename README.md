This is a python app that takes a screenshot of a given website.
Based on Python 3.7 


To download the Docker image from DockerHub, use the command below:

docker pull gabytal333/screenshot-app


To run the docker container, use the command below:
 
docker run --name app --mount type=bind,source="$(pwd)",target=/app gabytal333/screenshot-app "https://google.com"


#Replace "google.com" with any website that you want to take a screenshot from.
#The default location for the screenshot is your current directory that you run the docker run command from.
#to choose different location, You can change the "$pwd" with any directory on your host.

Gaby Tal.
