# flask_optional_routes

## This package allows you to specify optional routes in a url path.<br><br>

## How it works
Simply place a '?' delimiter at the end of a path segment and <br>
this code will automatically add rules for all possible routes.<br><br>

## How to install
* Method 1: Use PIP
```
pip install flask_optional_routes
```

* Method 2: 
Download from Github<br><br>

## Usage Example1
```python
from flask import Flask

from flask_optional_routes import OptionalRoutes


app = Flask(__name__)
optional = OptionalRoutes(app)

@optional.routes('/<user_id>/<user_name>?/')
def foobar(user_id, user_name=None):
    return 'it worked!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

Using @optional.routes('/<user_id>/<user_name>?/') <br>
the following urls will show the same endpoint:
* /1/
* /1/john/


## Usage Example2
```python
from flask import Flask

from flask_optional_routes import OptionalRoutes


app = Flask(__name__)
optional = OptionalRoutes(app)

@optional.routes('/a/b?/c/d?/')
def foobar():
    return 'it worked!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

Using @optional.routes('/a/b?/c/d?/') <br>
the following urls will show the same endpoint:
* /a/c/
* /a/b/c/
* /a/c/d/
* /a/b/c/d/
