import pytest

from alcherializer.exceptions import MalformedMetaClassException
from alcherializer.serializer import Serializer


def test_error_if_no_meta_class() -> None:
    class MySerializer(Serializer):
        pass

    with pytest.raises(MalformedMetaClassException):
        MySerializer()


def test_error_if_no_model_declared_at_meta_class() -> None:
    class MySerializer(Serializer):
        class Meta:
            pass

    with pytest.raises(MalformedMetaClassException):
        MySerializer()
