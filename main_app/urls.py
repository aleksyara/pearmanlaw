from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume_arbitrator/', views.resume_arbitrator, name='resume_arbitrator'),
    path('resume/', views.resume, name='resume'),
    path('clients/', views.clients, name='clients'),
    path('areasofpractice/', views.areasofpractice, name='areasofpractice'),
    path('articles/', views.articles, name='articles'),
    path('blog/', views.blog, name='blog'),
    path('blog/create/', views.PostCreate.as_view(), name='posts_create'), #handle GET & POST 
    path('links/', views.links, name='links'),
    path('contactus/', views.contactus, name='contactus'),
    path('prac_business/', views.prac_business, name='prac_business'),
    path('prac_publicworks/', views.prac_publicworks, name='prac_publicworks'),
    path('prac_transpo/', views.prac_transpo, name='prac_transpo'),
    path('prac_realestate/', views.prac_realestate, name='prac_realestate'),
    path('prac_domain/', views.prac_domain, name='prac_domain'),
    path('prac_finance/', views.prac_finance, name='prac_finance'),
    path('prac_construction/', views.prac_construction, name='prac_construction'),
    path('prac_publicagencies/', views.prac_publicagencies, name='prac_publicagencies'),
    path('prac_utilities/', views.prac_utilities, name='prac_utilities'),
    path('prac_litigation/', views.prac_litigation, name='prac_litigation'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy/', views.privacy, name='privacy'),
    path('admin/post/', views.post, name='post'),
    # New url pattern below for the NEW Users
    path('accounts/signup/', views.signup, name='signup'),
    
]