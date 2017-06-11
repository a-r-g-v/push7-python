# push7-python

push7 api client for python  
supporting python2.7 and python3.4

# Usage

```bash
pip install push7
```

## Initialize
First, you should create a client for push7. 
```python
from push7 import Client

appno = 'edit_your_appno'
apikey = 'edit_your_apps_apikey'

client = Client(appno, apikey)
```

## Create Push
```python
# Immediately 
client.push("title", "body", "http://arg.vc/icon.png", "http://arg.vc/").send()


# Create a reserved push ( push7 system will be send push to user after 4 hours)
from datetime import datetime, timedelta
target_datetime = datetime.now() + timedelta(hours=4)
client.push("title", "body", "http://arg.vc/icon.png", "http://arg.vc/", target_datetime).send()
```

## Create Push with Query

```python
from push7.push import PushWithQuery as query
parameters = ['user001', 'user002']
client.push_with_query("title", "body", "http://arg.vc/icon.png", "http://arg.vc/", query.Mode._or, parameters).send()
```


# For Contributors

## Testing

If you want to run tests, you should set environment vars 'PUSH7_APPNO' and 'PUSH7_APIKEY'.
After setting environment vars, you can run tests by below commands.

```bash
tox
```




## Pylint
```bash
cd push7
pylint * --disable=R,C,unused-import,locally-disabled
```

## Mypy
```bash
cd push7
mypy --ignore-missing-imports *.py
```

## Yapf
```bash
cd pushy
yapf -r -i push7/
```


