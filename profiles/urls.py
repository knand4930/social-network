from django.urls import path
from . import views

app_name ='profiles'

urlpatterns =[
    path("", views.my_profile_view, name="my_profile_view")
]