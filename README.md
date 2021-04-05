# facebook_breach

python3 -m venv fb_breach

cd fb_breach

open bin/activate in any text editor and set environment variables ie secret key, database credentials and all which are defined in the settings.py 
(Here i have used mysql database)

git clone https://github.com/sam007vns/facebook_breach.git

cd facebook_breach

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver
