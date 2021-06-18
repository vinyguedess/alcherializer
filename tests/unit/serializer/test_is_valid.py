from unittest import TestCase
import sqlalchemy
from alcherializer import Serializer, fields


class TestSerializerIsValidRequired(TestCase):

    def test_required_fields(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": "Fulano"
        })

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})

    def test_required_fields_are_filled(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": None
        })

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {
            "name": ["Can't be blank"]
        })

    def test_required_fields_ignore_except_fields(self) -> None:
        class MyModel:
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": "Fulano"
        })

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})


class TestSerializerClear(TestCase):

    def test_required_fields_are_filled(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": None
        })

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {
            "name": ["Can't be blank"]
        })

        serializer.clear()
        self.assertDictEqual(serializer.errors, {})


class TestSerializerDefiningValidator(TestCase):

    def test_defining_validator(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            name = fields.StringField()

            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": "Fulano"
        })

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})


class TestSerializerString(TestCase):

    def test_has_valid_length(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": "Fulano"
        })

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})

    def test_has_no_valid_length(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={
            "name": "Fulanos"
        })

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {
            "name": ["Limit of characters is 6"]
        })
