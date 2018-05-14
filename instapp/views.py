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


@login_required(login_url='/accounts/login/')
def settings(request):
    title = 'Insta-Gram'
    settings = Profile.get_profile()
    return render(request,'profile/settings.html',{"settings":settings,
                                                    "title":title,})



@login_required(login_url='/accounts/login/')
def edit(request):
    title = 'Insta-Gram'
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request,'profile/edit.html',{"title":title,
                                                "form":form})

@login_required(login_url="/accounts/login/")
def upload(request):
    title = 'Insta-Gram'
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = UploadForm()
            return render(request,'upload/new.html',{"title":title,
                                                    "user":current_user,
                                                    "form":form})



@login_required(login_url="/accounts/login/")
def search_results(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,
                                             "profiles":profile,
                                             "user":current_user,
                                             "username":searched_name})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_comment(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = current_user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {"user":current_user,
                                            "comment_form":form})
