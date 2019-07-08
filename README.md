# Flask-Maintenance

Adds maintenane mode capability to your Flask app.

## Installing:

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip install Flask-Maintenance
```

Then register this extension.

```
from flask_maintenance import Maintenance

app = Flask(__name__)
Maintenance(app)
```

Like other Flask extensions, you can register it lazily:

```
maintenance_mode = Maintenance()

def create_app():
    app = Flask(__name__)
    maintenance_mode.init_app(app)
```

## Usage

To enable Maintenance mode, run the following command:

```
$ flask maintenance enable
```

To disable Maintenance mode:

```
$ flask maintenance disable
```

## Custom template for Maintenance mode

To show a custom template to user when the maintenance mode is enabled, register a 503 [Custom Error Handler](http://flask.pocoo.org/docs/1.0/patterns/errorpages/#custom-error-pages).

```
from flask import render_template

@app.errorhandler(503)
def under_maintenance(e):
    return render_template('503.html'), 503
```

If you are using application factory pattern:

```
def under_maintenance(e):
    return render_template('503.html'), 503

def create_app():
    app = Flask(__name__)
    app.register_error_handler(503, under_maintenance)
    return app
```