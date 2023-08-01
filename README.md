# Intro
This project contains a simple Django REST framework web server which allows for tracking of financial trading transactions. In its simplest form, it will ingest a payload containing decimal parameters of "price", "quantity", and "symbol", then calculate the total transaction cost and add it to a database.

The project could be enhanced with an additional parameter of "purchased timestamp", indicating when the order was originally executed.


# Setup

> From within the 'drf_transactions' project folder containing 'manage.py', perform the following steps. 

#### Create & Activate Python3 virtual environment
The following commands will create a new Python3 virtual environment named 'env' and activate it. This allows for project-based isolation of your Python3 environment, ensuring a fresh installation for each project.
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
The following command will start the Django development web server, which runs on 0.0.0.0:8000 by default.
```
python manage.py runserver
```
This can be modified by specifying [address]:[port] following the 'runserver' parameter. For example, the following will start the web server on port 8443.
```
python manage.py runserver 0.0.0.0:8443
```

> Your Transactions webserver should now be running on 127.0.0.1:8000, unless a custom port was specified.

# Testing
#### Example POST
```
POST http://127.0.0.1:8000/transactions/
{
    "price": "35000.00",
    "quantity": ".000015"
}
```

#### Example List all Transactions
```
GET http://127.0.0.1:8000/transactions/
```
