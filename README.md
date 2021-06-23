[![Github Actions](https://github.com/vinyguedess/alcherializer/actions/workflows/main.yml/badge.svg)](https://github.com/vinyguedess/alcherializer/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/332cfdc498df9f6dc272/maintainability)](https://codeclimate.com/github/vinyguedess/alcherializer/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/332cfdc498df9f6dc272/test_coverage)](https://codeclimate.com/github/vinyguedess/alcherializer/test_coverage)

# Alcherializer
A "Django like" model serializer.

## Declaring Serializer
It's very simples to declare a serializer. Just like Django, the only
thing you need is to create a class with a Meta class inside and
a model attribute.

This instantly maps all fields declared in model.
```python
from datetime import datetime
from alcherializer import Serializer
import sqlalchemy


class User:
    name = sqlalchemy.Column(sqlalchemy.String(100))
    age = sqlalchemy.Column(sqlalchemy.Integer)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow)


class UserSerializer(Serializer):
    class Meta:
        model = User
```
PS: For further exemplifications we will always use **User** and **UserSerializer**.

## Data
Gets a dictionary of a single model.
```python
model = User(
    name="Clark Kent",
    age=31,
    is_active=True)

serializer = UserSerializer(model)
serializer.data  # { "name": "Clark Kent", ... }
```

Or, a list of models
```python
model = User(
    name="Clark Kent",
    age=31,
    is_active=True)

serializer = UserSerializer([model], many=True)
serializer.data  # [{ "name": "Clark Kent", ... }]
```

## Validation
To validate a payload, it's possible to send it through data argument while
instantiating the serializer and call **.is_valid** method.
```python
serializer = UserSerializer(data={
    "name": "Clark Kent",
    "age": 31,
    "is_active": True
})
serializer.is_valid()  # True
```

### Fetching validation errors
If any error happens you can fetch the information through error attribute.
```python
serializer = UserSerializer(data={
    "name": "", # If ommitted or None should present error too
    "age": 31,
    "is_active": True
})
serializer.is_valid()  # False
serializer.errors # {"name": ["Can't be blank"]}
```
