from django.urls import path, include
from rest_framework import routers
from .views.clientViewset import ClientViewSet
from .views.projectViewset import ProjectViewSet
from .views.usersViewset import UserViewSet

router = routers.DefaultRouter()
router.register(r'client',ClientViewSet)
router.register(r'project',ProjectViewSet, basename='project')
router.register(r'user',UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
