# Setup
#### Create & Activate Python3 virtual environment
```
python3 -m venv env
source env/bin/activate
```

#### Install Django and Django REST Framework
```
pip install django
pip install djangorestframework
```

#### Initialize Database
```
python manage.py makemigrations transactions
python manage.py migrate transactions
```

#### Run Development Web Server
```
python manage.py runserver
```

Your Transactions webserver should now be running on 127.0.0.1:8000
