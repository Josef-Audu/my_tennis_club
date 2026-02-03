from django.contrib import admin
from django.urls import path, include
from .members import views  # import your members app views

urlpatterns = [
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('admin/', admin.site.urls),
    path('', views.legacy, name='home'),  # <-- this makes the home page show members
    path('members/', include('my_tennis_club.members.urls')),  # optional if you still want /members/
]
