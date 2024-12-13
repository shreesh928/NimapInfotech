from rest_framework import viewsets
from django.contrib.auth import get_user_model
# from ..models.user import User
from ..serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)
