from django.shortcuts import render
from .serializers import MushroomSerializer
from mushroom.models import Mushroom
from .permissions import IsOwnerReadOnly
from rest_framework import generics

class MushroomList(generics.ListCreateAPIView):
  queryset = Mushroom.objects.all()
  serializer_class = MushroomSerializer
  
class MushroomDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerReadOnly,)
  queryset = Mushroom.objects.all()
  serializer_class = MushroomSerializer

