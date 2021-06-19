from unittest import TestCase
from alcherializer import fields


class TestFieldsBaseCast(TestCase):

    def test_cast(self) -> None:
        base_field: fields.BaseField = fields.BaseField()

        self.assertEqual(base_field.cast(10), 10)
        self.assertEqual(base_field.cast("10"), "10")
        self.assertEqual(base_field.cast(True), True)
