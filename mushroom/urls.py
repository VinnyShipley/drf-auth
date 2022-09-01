from django.urls import path
from .views import MushroomDetail, MushroomList

urlpatterns = [
  path('', MushroomList.as_view(), name='mushroom-list'),
  path('<int:pk>/', MushroomDetail.as_view(), name='mushroom-detail')
]