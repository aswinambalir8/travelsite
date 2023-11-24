from . import views
from django.urls import path

urlpatterns = [
    path('',views.func,name='func'),

]