from .models import Sign
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SignSerializer

class SignViewSet(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    permission_classes = [permissions.AllowAny]



