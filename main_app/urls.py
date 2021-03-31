from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume_arbitrator/', views.resume_arbitrator, name='resume_arbitrator'),
    path('admin/post/', views.post, name='post'),
]