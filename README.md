# newspaper-agency

Django project for creating and sharing news

## Check it out!

[Newspaper Agency project deployed to Render](https://newspaper-agency-853b.onrender.com)

You can use this test user
```
login: user
password: user12345
```

## Installation

Python 3 must be already installed

### Clone git repository

```shell
git clone https://github.com/msymonovych/newspaper-agency
cd newspaper_agency
```

### Create virtual environment and install dependencies

for unix
```shell
python3 -m venv venv
source venv/bin/acitvate
pip3 install -r requirements.txt
```
for windows
```shell
python -m venv venv
venv\Scripts\acitvate
pip install -r requirements.txt
```

### Migrations
```shell
python manage.py makemigrations
python manage.py migrate
```
### Start Django server
```shell
python manage.py runserver
```

## Features

* Authentication functionality for Publisher/User
* Creating news and sharing it directly from website interface
* Admin panel for advanced managing

## Demo

![demo](https://github.com/msymonovych/newspaper-agency/assets/87976005/9db3351e-2d30-469d-8871-aea6581033f9)
