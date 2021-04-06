from django.shortcuts import render
# from .models import Post

class Post():
  def __init__(self, title, description):
    self.title = title
    self.description = description
    # Add the foreign key linking to a user instance
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

posts = [
  Post('About COVID-19', 'We have already written the code to respond using the render method in the view.'),
  Post('US Benefits', 'Now the fun stuff. We will type it in if there is time, otherwise we will copy/paste and review:')
]

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'index.html', { 'posts': posts })

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

def post(request):
    return render(request, 'post.html')