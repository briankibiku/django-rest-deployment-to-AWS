from django.urls import path
from profiles_api import views

urlpatterns = [
     path('hello-view/', view=views.HelloApiView.as_view(), name='')
]