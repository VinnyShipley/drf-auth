from django.db import models
from django.contrib.auth import get_user_model

class Mushroom(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
  name = models.CharField(max_length=256)
  flavor = models.CharField(max_length=256)
  picked_time = models.DateTimeField(auto_now_add=True)
  update_info = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
