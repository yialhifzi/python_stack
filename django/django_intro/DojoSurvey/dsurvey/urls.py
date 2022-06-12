from django.urls import path     
from . import views

urlpatterns = [
    path('', views.root),
    path('DojoSurvey', views.index),
    path('result',views.create_user),
]
