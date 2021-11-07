import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from alcherializer import (
    Serializer,
    fields,
)


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


def test_data_get_related_one_to_one_model() -> None:
    class MyRelatedModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        hello = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_related_model"

    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
        related_id = sqlalchemy.Column(
            sqlalchemy.Integer, sqlalchemy.ForeignKey(MyRelatedModel.id)
        )

        related = relationship(MyRelatedModel, uselist=False)

        __tablename__ = "my_model"

    class MyRelatedModelSerializer(Serializer):
        class Meta:
            model = MyRelatedModel

    class MyModelSerializer(Serializer):
        related = MyRelatedModelSerializer()

        class Meta:
            model = MyModel
            fields = ["id", "name", "related"]

    model = MyModel(
        id=1,
        name="my name",
        related=MyRelatedModel(
            id=1,
            hello="world",
        ),
    )

    serializer = MyModelSerializer(model)
    assert serializer.data == {
        "id": 1,
        "name": "my name",
        "related": {"id": 1, "hello": "world"},
    }


def test_data_get_related_has_many_models() -> None:
    class MyRelatedModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        hello = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        __tablename__ = "my_related_model"

    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
        related_id = sqlalchemy.Column(
            sqlalchemy.Integer, sqlalchemy.ForeignKey(MyRelatedModel.id)
        )

        related = relationship(MyRelatedModel, uselist=False)

        __tablename__ = "my_model"

    class MyRelatedModelSerializer(Serializer):
        class Meta:
            model = MyRelatedModel

    class MyModelSerializer(Serializer):
        related = MyRelatedModelSerializer()

        class Meta:
            model = MyModel
            fields = ["id", "name", "related"]

    model = MyModel(
        id=1,
        name="my name",
        related=[
            MyRelatedModel(
                id=1,
                hello="world",
            ),
        ],
    )

    serializer = MyModelSerializer(model)
    assert serializer.data == {
        "id": 1,
        "name": "my name",
        "related": [
            {"id": 1, "hello": "world"},
        ],
    }


def test_data_get_method_fields() -> None:
    class MyModel(declarative_base()):
        id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, nullable=False
        )
        first_name = sqlalchemy.Column(sqlalchemy.String)
        last_name = sqlalchemy.Column(sqlalchemy.String)

        __tablename__ = "my_model"

    class MyModelSerializer(Serializer):
        full_name = fields.MethodField()

        def get_full_name(self, obj: MyModel):
            return f"{obj.first_name} {obj.last_name}"

        class Meta:
            model = MyModel
            fields = ["id", "full_name"]

    model = MyModel(id=1, first_name="hello", last_name="world")

    serializer = MyModelSerializer(model)
    assert serializer.data == {"id": 1, "full_name": "hello world"}
