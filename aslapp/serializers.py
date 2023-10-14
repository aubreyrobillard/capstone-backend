from .models import Sign
from rest_framework import serializers

class SignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sign
        fields = ['id', 'image', 'name', 'notes', 'date']