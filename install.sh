# Install Centos
# First you need the image
# sudo apt-get install docker -y
# snap install docker
# docker pull centos # Replace for Ubuntu
# docker run -d -t --name cantcontainmyself centos
# docker ps
# docker exec -it cantcontainmyself bash

# docker pull alpine # Replace for Ubuntu
# docker run -d -t --name ohyeah alpine
# docker exec -it ohyeah sh


# docker pull thenetworkchuck/nccoffee:frenchpress
# # [host_port:docker_container]
# # docker -p [Port] -- [Name of the Container] [IMG name or Distro]
# docker run -d -t -p 80:80 --name nccoffee thenetworkchuck/nccoffee:frenchpress
# docker stop nccoffee
# docker stats

# Install Alpine

# Mistery think


sudo apt-get install docker-compose 



# Updating Stuff
# ----------------------------------------------------------------------
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

# Virtual Environment Set Up
# ----------------------------------------------------------------------
sudo apt-get install -y python3-pip
sudo apt-get install python3-venv -y

# Packages installation into Virtual env
# ----------------------------------------------------------------------
cd /pdf-rendering-service/flask
python3 -m venv env
source env/bin/activate

# Linux Packs
# ----------------------------------------------------------------------
sudo apt-get install poppler-utils -y
sudo apt-get install redis -y
sudo apt-get install uwsgi -y

# Python Packs
# ----------------------------------------------------------------------
pip3 install flask
pip3 install uwsgi
pip3 install pdf2image
pip3 install python-magic
pip3 install redis
pip3 install rq

deactivate
cd /pdf-rendering-service

# Create and Run the Services
# ----------------------------------------------------------------------
sudo cp /pdf-rendering-service/flask/services/app.service /etc/systemd/system/app.service
sudo cp /pdf-rendering-service/flask/services/rqworker.service /etc/systemd/system/rqworker.service
sudo service app start
sudo service rqworker stars
sudo systemctl daemon-reload
sudo service app restart
sudo service rqworker restart
echo 'Completed Services'
sudo service app status
sudo service rqworker status

# Docker Stuff
# ----------------------------------------------------------------------

sudo rm -r Dockerfile
sudo rm -r .dockerignore


touch .dockerignore
echo "env/
__pycashe__" >> .dockerignore


touch Dockerfile
echo "FROM python:3.7.2-strech

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD 
" >> .Dockerfile

touch app.ini
echo "[uwsgi]
wsgi-file = pdf_flask_service.py
socket = :8080
processes = 4
threads = 2
master = true
chmod-socket = 660
vacuum = true
die-on-term = true
" >> .Dockerfile

export FLASK_APP=run.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
