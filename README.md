# GingerPaymentAssignment
Python Flask Restful Api.

## Concept

Sqlite DB is used for storing data. Sqlalchemy is used to help with the queries. I have used a service layer which is an internal API of this system. On top of this internal API, I have implemented two  applications. 
1. Restful API
2. Frontend

Restful API is used for CRUD operations. Frontend application is used for serving static files(CSS, JS, HTML) and is also responsible for routing as I have not used any frontend routing solution.
All api endpoints are hidden behind authentication. Currently using cookies based session and authentication. So the API can be tested in browser easily for now. Can easily switch to Token based authentication (Will do it if found time). 

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [Sqlite](https://sqlite.org)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone git@github.com/syedwaseemjan/GingerPaymentAssignment.git
    $ cd GingerPaymentAssignment

#### 2. Create and initialize virtualenv for the project:

    $ mkdir ginger_virtualenv
    $ virtualenv ginger_virtualenv
    $ source ginger_virtualenv/bin/activate
    $ pip install -r requirements.txt

#### 3. Setup the Sqlite DB (Add default admin user):

    $ python manage.py create_db
    $ python manage.py init_db

#### 4. Run the server:

    $ python runserver.py

#### 5. Load the system in browser:

    $ Visit http://127.0.0.1:5000
    $ Username: admin@gingerassignment.com
    $ Password: test123

