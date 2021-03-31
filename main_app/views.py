from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'index.html')

# def about(request):
#   return HttpResponse('<h1>This is About Page</h1>') # simmiluar to res.send

def resume_arbitrator(request):
    return render(request, 'resume_arbitrator.html') #instead of HTTPResponse we can use a template

def post(request):
    return render(request, 'post.html')