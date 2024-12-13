from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Project
from ..serializers import ProjectsSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)




