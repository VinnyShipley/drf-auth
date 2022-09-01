import imp
from rest_framework.serializers import ModelSerializer
from .models import Mushroom

class MushroomSerializer(ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'flavor', 'picked_time',)
    model = Mushroom
