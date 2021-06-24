from unittest import TestCase
from alcherializer import fields


class TestFieldsBooleanCast(TestCase):

    def test_cast_true_value(self) -> None:
        bool_field: fields.BooleanField = fields.BooleanField()

        self.assertTrue(bool_field.cast("True"))
        self.assertTrue(bool_field.cast("T"))
        self.assertTrue(bool_field.cast("true"))
        self.assertTrue(bool_field.cast("t"))
        self.assertTrue(bool_field.cast(True))
        self.assertTrue(bool_field.cast(1))
        self.assertTrue(bool_field.cast("1"))

    def test_cast_false_value(self) -> None:
        bool_field: fields.BooleanField = fields.BooleanField()

        self.assertFalse(bool_field.cast("False"))
        self.assertFalse(bool_field.cast("F"))
        self.assertFalse(bool_field.cast("false"))
        self.assertFalse(bool_field.cast("f"))
        self.assertFalse(bool_field.cast(False))
        self.assertFalse(bool_field.cast(0))
        self.assertFalse(bool_field.cast("0"))

    def test_cast_invalid_boolean_value(self) -> None:
        bool_field: fields.BooleanField = fields.BooleanField()

        self.assertNotIsInstance(bool_field.cast("abc"), bool)
