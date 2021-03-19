from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from events.models import EventUser
from events.serializers import EventUserCreateSerializer
from common.mixins import SerializerClassMixin


class EventUserViewSet(CreateModelMixin, GenericViewSet, SerializerClassMixin):
    queryset = EventUser.objects.all()
    serializer_class = EventUserCreateSerializer
