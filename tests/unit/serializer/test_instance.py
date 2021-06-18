from unittest import TestCase
from alcherializer.serializer import Serializer
from alcherializer.exceptions import MalformedMetaClassException


class TestSerializerInstance(TestCase):

    def test_error_if_no_meta_class(self) -> None:
        class MySerializer(Serializer):
            pass

        self.assertRaises(
            MalformedMetaClassException,
            lambda: MySerializer())

    def test_error_if_no_model_declared_at_meta_class(self) -> None:
        class MySerializer(Serializer):
            class Meta:
                pass

        self.assertRaises(
            MalformedMetaClassException,
            lambda: MySerializer())