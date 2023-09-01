from rest_framework import serializers
from .models import Lister

class ListerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lister
        fields = ['id', 'email', 'user_name', 'date_joined']