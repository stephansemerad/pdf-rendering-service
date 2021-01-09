sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv
sudo apt-get install python3-venv -y
cd flask
python3 -m venv env
source env/bin/activate
sudo pip3 install flask

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
