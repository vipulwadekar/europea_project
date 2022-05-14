from django.contrib import admin
from django.urls import path,include
from .views import views
urlpatterns = [
    path('',views.get_user),
    path('create-user',views.post_user)

]
