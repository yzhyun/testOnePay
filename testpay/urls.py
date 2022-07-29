from django.urls import path, include
from . import views
app_name = 'testpay'
urlpatterns = [
    path('', views.testMain.as_view(), name='testMain'),
    path('pc2app/', views.testPc2App.as_view(), name='testPc2App'),

]
