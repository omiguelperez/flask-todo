# flask-intro

Flask introduction project

## Run 

- Set file with flask app `export FLASK_APP=filename.py`
- Enable debug mode `export FLASK_DEBUG=1`
- Run in development environment`FLASK_ENV=development`

# Testing

Run tests with `unittest` defining an app command:

```python
import unittest

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover(TEST_DIR_PATH)
    unittest.TextTestRunner().run(tests)
```