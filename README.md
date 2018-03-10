test-flask-website
==================

A simple Flask website based on the [tutorial][1] for testing Travis CI with.

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

[1]: http://flask.pocoo.org/docs/0.12/tutorial/
