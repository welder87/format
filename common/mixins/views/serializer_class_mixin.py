from typing import Type

from rest_framework.serializers import Serializer


class SerializerClassMixin:
    serializer_classes = {}

    def get_serializer_class(self) -> Type[Serializer]:
        return self.serializer_classes.get(self.action, self.serializer_class)
