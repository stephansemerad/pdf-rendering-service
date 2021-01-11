# Updating Stuff
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install -y python3-pip

# # Linux Stuff
# sudo apt-get install poppler-utils -y
# sudo apt-get install redis -y

# # Python Local Stuff
# sudo pip3 install virtualenv
# sudo pip3 install pdf2image
# sudo pip3 install python-magic
# sudo pip3 install redis
# sudo pip3 install rq


# App Build Up
# ----------------------------------------------------------------------

cd /pdf-rendering-service/flask
sudo apt-get install python3-venv -y
python3 -m venv env
source env/bin/activate
sudo apt-get install poppler-utils -y
sudo apt-get install redis -y
sudo apt-get install uwsgi -y

pip3 install flask
pip3 install uwsgi
pip3 install pdf2image
pip3 install python-magic
pip3 install redis
pip3 install rq

deactivate
cd /pdf-rendering-service



# Services
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
