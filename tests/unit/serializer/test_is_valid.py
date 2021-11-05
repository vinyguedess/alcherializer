from unittest import TestCase

import sqlalchemy

from alcherializer import (
    Serializer,
    fields,
)


class TestSerializerIsValidRequired(TestCase):
    def test_required_fields(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": "Fulano"})

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})

    def test_required_fields_are_filled(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": None})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {"name": ["Can't be blank"]})

    def test_required_fields_ignore_except_fields(self) -> None:
        class MyModel:
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": "Fulano"})

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})


class TestSerializerClear(TestCase):
    def test_required_fields_are_filled(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": None})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {"name": ["Can't be blank"]})

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

        serializer = MySerializer(data={"name": "Fulano"})

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})


class TestSerializerBoolean(TestCase):
    def test_is_a_valid_true_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": True})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_true_string_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": "true"})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_true_integer_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": 1})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_false_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": False})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_false_string_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": "false"})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_false_integer_boolean(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": 0})

        self.assertTrue(serializer.is_valid())

    def test_is_a_valid_boolean_error_if_not_a_castable_value(self) -> None:
        class MyModel:
            is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"is_active": "abc"})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(
            serializer.errors, {"is_active": ["Not a valid boolean"]}
        )


class TestSerializerString(TestCase):
    def test_has_valid_length(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": "Fulano"})

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {})

    def test_has_no_valid_length(self) -> None:
        class MyModel:
            name = sqlalchemy.Column(sqlalchemy.String(6), nullable=False)

        class MySerializer(Serializer):
            class Meta:
                model = MyModel

        serializer = MySerializer(data={"name": "Fulanos"})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(
            serializer.errors, {"name": ["Limit of characters is 6"]}
        )
