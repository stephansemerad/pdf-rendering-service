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
echo "env/
__pycashe__" >> .dockerignore