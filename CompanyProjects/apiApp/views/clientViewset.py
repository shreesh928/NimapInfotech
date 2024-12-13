from rest_framework.permissions import IsAuthenticated
from ..models import Client
from ..serializers import ClientSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)