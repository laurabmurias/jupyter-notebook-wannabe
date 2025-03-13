#!/bin/bash

# Default container, image and volume names
CONTAINER_NAME="pretty-container"
IMAGE_NAME="jupnotebook-wannabe"
VOLUME="$HOME/path/to/project/root/dir"
LOCAL_PORT=5000
DOCKER_PORT=5000

rebuild_image() {
    echo "Rebuilding the Docker image..."
    docker build -t $IMAGE_NAME .
}

run_container() {
    echo "Running the container..."
    docker run -v $VOLUME:/app -d -p $LOCAL_PORT:$DOCKER_PORT --name $CONTAINER_NAME $IMAGE_NAME
    sleep 3
    docker logs $CONTAINER_NAME
}

stop_and_remove_container() {
    if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
        echo "Stopping and removing existing container..."
        docker stop $CONTAINER_NAME
        docker rm $CONTAINER_NAME
    fi
}

# Parse flags
while getopts "r" flag; do
    case $flag in
        r)
            stop_and_remove_container
            rebuild_image
            run_container
            exit 0
            ;;
        *)
            stop_and_remove_container
            run_container
            exit 0
            ;;
    esac
done

if [ "$OPTIND" -eq 1 ]; then
    stop_and_remove_container
    run_container
fi
