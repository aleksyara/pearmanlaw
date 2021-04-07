from django.shortcuts import render
#import this to crete a view, update, delete..
from django.views.generic.edit import CreateView
from .models import Post


# Create your views here.
# Add the following import
from django.http import HttpResponse

class PostCreate(CreateView):
  model = Post #it creates Model Form that will be injected -> main_app/cat_form.html
  fields = '__all__' # fileds generetaed in the modelForm
  # fields = ['title', 'description']
  # ^^^ __all__ - specify that the form should contain all of the Cat Model's attributes
  #OR if you want to display at the form only specific fields = ['name', 'breed', 'description', 'age']
  # success_url = '/cats/' - this is one wat to redirect. 
  #However, we can utilize to kwargs={'cat_id': self.id} in the models.py


# Define the home view
def home(request):
  return render(request, 'index.html')

# def about(request):
#   return HttpResponse('<h1>This is About Page</h1>') # simmiluar to res.send

def resume_arbitrator(request):
    return render(request, 'resume_arbitrator.html') 

def resume(request):
    return render(request, 'resume.html') 

def clients(request):
    return render(request, 'clients.html') 

def areasofpractice(request):
    return render(request, 'areasofpractice.html') 

def articles(request):
    return render(request, 'articles.html') 

def blog(request):
  posts = Post.objects.all()
  return render(request, 'blog.html', { 'posts': posts })   

def links(request):
    return render(request, 'links.html')     

def contactus(request):
    return render(request, 'contactus.html')    

def prac_business(request):
    return render(request, 'prac_business.html') 

def prac_publicworks(request):
    return render(request, 'prac_publicworks.html')  

def prac_transpo(request):
    return render(request, 'prac_transpo.html')  

def prac_realestate(request):
    return render(request, 'prac_realestate.html')   

def prac_domain(request):
    return render(request, 'prac_domain.html')  

def prac_finance(request):
    return render(request, 'prac_finance.html')  

def prac_construction(request):
    return render(request, 'prac_construction.html')  

def prac_publicagencies(request):
    return render(request, 'prac_publicagencies.html')  

def prac_utilities(request):
    return render(request, 'prac_utilities.html')  

def prac_litigation(request):
    return render(request, 'prac_litigation.html')  

def disclaimer(request):
    return render(request, 'disclaimer.html') 

def privacy(request):
    return render(request, 'privacy.html') 

def post(request):
    return render(request, 'post.html')