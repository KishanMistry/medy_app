# Medy App - To upload medical product for re-sell it

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KishanMistry/medy_app.git
$ cd medy_app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip3 install -r requirements.txt
```
# Database 

I have used MySQL database for this project. Create a database with the name " medy_app "
Run below command to create migrations

```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Once `migration` has finished downloading the dependencies:
```sh
$ (venv)$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/` in browser.