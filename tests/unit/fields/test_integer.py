from unittest import TestCase
from alcherializer import fields


class TestFieldsIntegerCast(TestCase):

    def test_cast(self) -> None:
        int_field: fields.IntegerField = fields.IntegerField()

        self.assertEqual(
            int_field.cast(10),
            10)

    def test_cast_when_value_isnt_a_number_type(self) -> None:
        int_field: fields.IntegerField = fields.IntegerField()

        self.assertEqual(
            int_field.cast("10"),
            10)

    def test_cast_when_value_is_boolean(self) -> None:
        int_field: fields.IntegerField = fields.IntegerField()

        self.assertEqual(int_field.cast(True), 1)
        self.assertEqual(int_field.cast(False), 0)

    def test_cast_if_value_is_none_return_zero(self) -> None:
        int_field: fields.IntegerField = fields.IntegerField()

        self.assertEqual(int_field.cast(None), 0)
