from django.urls import path

from rest_framework import routers
from . import views

router = routers.SimpleRouter()

# router.register('articles', views.index)


urlpatterns = [
    path('articles/', views.index, name="article"),
]
