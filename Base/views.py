from django.shortcuts import redirect, render
from django.contrib.auth import  logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project
from .models import Certification
from .models import Skill
from .models import About
from .models import Contact

import os
from django.http import HttpResponse, FileResponse
from django.conf import settings
# Create your views here.

def home(request):
   return render(request, 'home.html')

def projects(request):
   projects = Project.objects.all()    
   return render(request, 'projects.html', {'projects': projects})

def contact(request):
   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']

      msg = Contact.objects.create()
      msg.fullname = name
      msg.email = email
      msg.message = message
      msg.save()
      messages.success(request, "Login has been created.")
      return redirect('/')

   return render(request, 'contact.html')


def about(request):
   certifications = Certification.objects.all()    
   skills = Skill.objects.all()
   about = About.objects.first()     
   return render(request, 'about.html', {'certifications': certifications, 'skills': skills, 'about': about})

def login_view(request): 
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
         auth_login(request, user)
         return redirect('/')
      messages.error(request, "Invalid credentials")

   return render(request, 'login.html')

def signup(request):
   
   if request.method == "POST":
      username = request.POST['name']
      email = request.POST['email'] 
      password1 = request.POST['password']
      password2 = request.POST['confirm']

      if password1 == password2:
         if User.objects.filter(username=username).exists():
               messages.error(request, "Username already exists")
         elif User.objects.filter(email=email).exists():
               messages.error(request, "Email already registered")
         else:
               user = User.objects.create_user(username=username, email=email, password=password1)
               user.save()
               messages.success(request, "Account created successfully")
               return redirect('/login')
      else:
         messages.error(request, "Passwords do not match")

   return render(request, 'signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def serve_cv(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv', file_name)
    
    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    else:
        # Return a 404 if the file is not found
        return HttpResponse("File not found", status=404)