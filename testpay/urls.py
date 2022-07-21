from django.urls import path
from . import views
app_name = 'testpay'
urlpatterns = [
    path('main/', views.testMain.as_view(), name='testmain'),
]
