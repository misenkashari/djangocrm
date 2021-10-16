from django.urls import path
from .views import upload_file
from django.contrib.auth.decorators import login_required



app_name = "csvs"
urlpatterns =[
    path('', login_required(upload_file), name='csv'),
]