# RENTAL HOUSING MANAGEMENT

# Set Up Development With Docker

1. Download Docker from [here](https://docs.docker.com/)
2. Set up an account to download Docker
3. Install Docker after download
4. Go to your terminal run the command `docker login`
5. Input your Docker email and password

To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the dir
-   create a `.env` file from the template `.env.example` and update the variables
-   `docker-compose build` to build the application images
-   `docker-compose up -d` to start the api after the previous command is successful
- GO to the url `http://0.0.0.0:5000` to access the api

The `docker-compose build` command builds the docker image where the api and its postgres database would be situated.

The `docker-compose up -d` command starts the application 

To stop the running containers run the command `docker-compose down`

