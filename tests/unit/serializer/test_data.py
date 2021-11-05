from unittest import TestCase

import sqlalchemy

from alcherializer import Serializer


class TestSerializerData(TestCase):
    def test_data_single_instance(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        model = MyModel()
        model.name = "hello world"

        serializer = MySerializer(model)
        self.assertDictEqual(serializer.data, {"name": "hello world"})

    def test_data_multiple_instances(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        model = MyModel()
        model.name = "hello world"

        serializer = MySerializer([model], many=True)
        self.assertListEqual(serializer.data, [{"name": "hello world"}])
