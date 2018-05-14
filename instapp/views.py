from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Insta-Gram'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'index.html',{"title":title,
                                        "profile":profile,
                                        "comments":comments,
                                        "current_user":current_user,
                                        "images":image,})

@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'Insta-Gram'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'profile/profile.html',{"title":title,
                                                  "comments":comments,
                                                  "image":image,
                                                  "user":current_user,
                                                  "profile":profile,})
