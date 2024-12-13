from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.timezone import now



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"



class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'created_at', 'created_by']




User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        read_only_fields = ['date_joined']

    

