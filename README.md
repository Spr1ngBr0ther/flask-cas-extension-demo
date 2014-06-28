# flask-cas-extension-demo

A simple flask app to demo CAS login using the Flask-CAS extension

[Live demo](http://flask-cas-extension-demo.cameronbwhite.com)

## Installation

1. Clone it `git clone https://github.com/cameronbwhite/flask-cas-extension-demo`
2. Enter it `cd flask-cas-extension-demo`
3. Create python virtual environment `virtualenv venv`
4. Activate virtual environment `source venv/bin/activate`
5. Install it and dependencies `python setup.py install`

## Running

There are a few ways to run the application. The first way is to run it in
flask's web server. The second way is to use gunicorn. Its also all set
up to run on Heroku.

### Flask web server (NOT FOR PRODUCTION)

If your CAS is located at `https://sso.pdx.edu/`

```sh
python app.py --debug True
```

### Gunicorn

If your CAS is located at `https://sso.pdx.edu/`

You need to add an environment variable `SECRET_KEY`
before you can run gunicorn.

1. Add `SECRET_KEY` `export SECRET_KEY=[its a secret]`
2. Run it `gunicorn app:app`

### Heroku

Its ready to go. All you have to do is make an account and upload it.
You will need to set up the enviroment like gunicorn.

