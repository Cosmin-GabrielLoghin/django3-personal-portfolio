from django.urls import path
from . import views

urlpatterns = [

    path('', views.userandpass, name='userandpass' ),
    
    
]
