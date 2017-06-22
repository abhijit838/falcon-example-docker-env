### Falcon Docker Development Environment
Simulation of falcon examples in side a docker env
App can be run from command line using docker and without docker
 
#### Run App Using Docker - Preferable if developer system does not support gunicorn(windows))
    * Install git
    * Install docker 
    * Install docker-compose
    $ git clone https://github.com/abhijit838/falcon-example-docker-env.git
    * Change directory to project root directory
    $ docker-compose up
    
#### Run App Without Docker
    * Install git
    $ git clone <url>
    * Change directory to project root directory
    $ gunicorn api.wsgi:app --bind 0.0.0.0:8080 --workers 3 --reload