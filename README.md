This is a python app that takes a screenshot of a given website.
Based on Python 3.7 

To download the Docker image from DockerHub, use the command below:

docker pull gabytal333/screenshot-app


To run the docker container, use the command below:
 
docker run --name app --mount type=bind,source="$(pwd)",target=/opt gabytal333/screenshot-app "https://google.com"

#Replace "google.com" with any website that you want to take a screenshot from.
#Do not forget to add the tight protocol scheme (http:// or https://) or you will get an error.

#The default location for the screenshot to be saved is your current directory that you run the docker run command from,
to choose a different location, You can change the "$pwd" with any directory on your host.

#For heavy websites with a large static content, please add the docker shared memory parameter. "--shm-size *g"
For example: docker run --name app --mount type=bind,source="$(pwd)",target=/opt --shm-size 2g screenshot-app "https://www.walla.co.il" 

Gaby Tal.
