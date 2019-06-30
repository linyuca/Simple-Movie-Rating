#FROM python:2.7-alpine
FROM python:3-alpine3.10
#FROM python:3-slim

#ENV MY_KEY $MY_KEY

RUN pip install requests
WORKDIR /usr/src/app
COPY movie.py ./

ENTRYPOINT ["python", "./movie.py"]

# build it
#  docker build --build-arg MY_KEY=$MY_KEY -t my-image .
#  docker build -t my-image .

# run it
# docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'The Godfather'

# delete container
# docker container prune

# delete images
# docker image rm <image id>

