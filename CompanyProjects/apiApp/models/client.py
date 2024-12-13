from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        null=True,  # Allow NULL values
        blank=True, # Allow blank values in forms
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.client_name