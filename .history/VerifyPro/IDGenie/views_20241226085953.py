from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .models import BlogPost, Comment # Import your BlogPost model
from .forms import  CustomUserCreationForm
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
# views.py

# Create your views here.
def index(request):
    # Fetch the welcoming page of the site
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/index.html', {'blog_posts': blog_posts})


def blogpost(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'IDGenie/blogpost.html', {'blog_posts': blog_posts})


def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()
    images = blog_post.images.all()

    if request.method == 'POST' and request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.blog_post = blog_post
            comment.author = request.user
            comment.save()
            # Return the comment details as JSON
            return JsonResponse({
                'success': True,
                'username': comment.author.username,
                'profile_picture': comment.author.profile_picture.url if comment.author.profile_picture else None,
                'created_at': comment.created_at.strftime('%B %d, %Y at %I:%M %p'),
                'content': comment.content
            })

        return JsonResponse({'success': False, 'errors': form.errors})

    form = CommentForm()
    return render(request, 'IDGenie/blog_detail.html', {
        'blog_post': blog_post,
        'comments': comments,
        'images': images,
        'form': form,
    })



# Login code

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('IDGenie:index')  # Redirect to home or dashboard page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'IDGenie/login.html', {'form': form})




def custom_logout(request):
    logout(request)
    return redirect('IDGenie:index')  # Redirect to login page after logging out


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Debugging: Check form validation success
            print("Form is valid!")  # Add this for debugging
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            messages.success(request, 'Your account has been created successfully!')
            return redirect('/')  # Redirect to the desired page (like home or dashboard)
        else:
            # Debugging: Check form errors
            print(form.errors)  # Add this to check form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            
            return render(request, 'IDGenie/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()  # Create an empty form for GET requests
    return render(request, 'IDGenie/signup.html', {'form': form})
