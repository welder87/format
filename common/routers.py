from rest_framework import routers

from events import views

router = routers.DefaultRouter()
router.register(r'event_user', views.EventUserViewSet)
