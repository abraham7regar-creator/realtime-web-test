from rest_framework import generics

from . import models
from . import serializers

# Create your views here.

class AppList(generics.ListCreateAPIView):
    queryset = models.App.objects.all()
    serializer_class = serializers.AppSerializer

class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.App.objects.all()
    serializer_class = serializers.AppSerializer
