from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [

    #path('CJP-PM-001/', views.ApiGetList.as_view(), name='PM001'),
    path('PM1001/', views.post),
    path('PM1005/', views.post),
    path('PM1023/', views.post),


]
