import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from alcherializer import Serializer


def test_data_single_instance() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    model = MyModel()
    model.id = 1
    model.name = "hello world"

    serializer = MySerializer(model)
    assert serializer.data == {"id": 1, "name": "hello world"}


def test_data_multiple_instances() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel

    model = MyModel()
    model.id = 1
    model.name = "hello world"

    serializer = MySerializer([model], many=True)
    assert serializer.data == [{"id": 1, "name": "hello world"}]


def test_data_get_only_declared_fields_if_declared() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_model"

    class MySerializer(Serializer):
        class Meta:
            model = MyModel
            fields = ["id"]

    model = MyModel()
    model.id = 1
    model.name = "hello world"

    serializer = MySerializer(model)
    assert serializer.data == {"id": 1}
