test-flask-website
==================

Testing for a Flask website

Developing
----------
On Windows:
```
> git clone git@github.com:samuelharmer/test-flask-website.git
> cd test-flask-website
> virtualenv venv
> venv\Scripts\activate
(venv) > set FLASK_APP=website
(venv) > set FLASK_DEBUG=true
(venv) > pip install --editable .
(venv) > flask initdb
(venv) > flask run
```
