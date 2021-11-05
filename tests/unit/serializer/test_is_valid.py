import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from alcherializer import (
    Serializer,
    fields,
)


def test_required_fields() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": "Fulano"})

    assert serializer.is_valid()
    assert serializer.errors == {}


def test_required_fields_are_filled() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": None})

    assert serializer.is_valid() is False
    assert serializer.errors == {"name": ["Can't be blank"]}


def test_required_fields_ignore_except_fields() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": "Fulano"})

    assert serializer.is_valid()
    assert serializer.errors == {}


def test_required_fields_are_filled_and_clearing_serializer() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": None})

    assert serializer.is_valid() is False
    assert serializer.errors == {"name": ["Can't be blank"]}

    serializer.clear()
    assert serializer.errors == {}


def test_defining_validator() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        name = fields.StringField()

        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": "Fulano"})

    assert serializer.is_valid()
    assert serializer.errors == {}


def test_is_a_valid_true_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": True})

    assert serializer.is_valid()


def test_is_a_valid_true_string_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": "true"})

    assert serializer.is_valid()


def test_is_a_valid_true_integer_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": 1})

    assert serializer.is_valid()


def test_is_a_valid_false_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": False})

    assert serializer.is_valid()


def test_is_a_valid_false_string_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": "false"})

    assert serializer.is_valid()


def test_is_a_valid_false_integer_boolean() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": 0})

    assert serializer.is_valid()


def test_is_a_valid_boolean_error_if_not_a_castable_value() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"is_active": "abc"})

    assert serializer.is_valid() is False
    assert serializer.errors == {"is_active": ["Not a valid boolean"]}


def test_has_valid_length() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": "Fulano"})

    assert serializer.is_valid()
    assert serializer.errors == {}


def test_has_no_valid_length() -> None:
    class MyModel:
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    serializer = MySerializer(data={"name": "Fulanos"})

    assert serializer.is_valid() is False
    assert serializer.errors == {"name": ["Limit of characters is 6"]}
