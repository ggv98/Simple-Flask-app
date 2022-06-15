# Simple Flask API

Flask API for extracting images from image URLs and saving image details in Postgres database storage.

Information for each image contains:
-  sha1 value of the file;
-  image dimensions;
-  image type;

## How to run 

To start the server with all necessary containers go to the main project directory and execute:

     docker-compose up

## Swagger documentation
Swagger documentation can be accessed at the following URL:
    
http://localhost:5000/api/docs/

## pgadmin configuration
pgadmin container will be started as part of docker-compose <br />

It can be accessed at the following URL:

http://localhost:5050

Default pgadmin credential:
- Email: user@user.com
- Password: root

Server configuration:
- host name -> postgres_container
- port -> 5432
- username -> user
- password -> password

# Example:
Endpoint URL: -> localhost:5000/api/v1/images


Request body:
    
    {
        "url": "https://images.pexels.com/photos/3762839/pexels-photo-3762839.jpeg?cs=srgb&dl=pexels-shiny-diamond-3762839.jpg&fm=jpg",
        "confirm": true 
    }

To execute image download in the background you can set "confirm" parameter to false. This way you will get confirmation that the request is accepted but no information whenever detail extraction is successful.

