from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>', views.details, name='details'),# maps /members/ to members view
    path('', views.members, name='members-list'),
]
