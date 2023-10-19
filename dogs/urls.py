from django.urls import path
from .views import *

urlpatterns = [
    path('dogs/', DogList.as_view()),
    path('dogs/<int:pk>', DogDetail.as_view()),
    path('breeds/', BreedList.as_view()),
    path('breeds/<int:pk>', BreedDetail.as_view()),
]