from django import forms
from .models import BlogPost, Comment
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Form for handling BlogPost in the Admin interface


class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'video_url', 'author']  # 'quote' removed since CKEditor handles rich content
        widgets = {
            'content': CKEditorWidget(),  # Using CKEditor for the content field
        }

    # Custom save method to handle extra fields (if needed)
    def save(self, commit=True):
        blog_post = super().save(commit=False)

        # Any additional processing for media (like saving images or video URLs) can go here
        if commit:
            blog_post.save()

        return blog_post


# Form for handling Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )  
    
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Additional fields for first name, last name, gender, phone number, and profile picture
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=True)
    phone_number = forms.CharField(max_length=15)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'gender', 'phone_number', 'profile_picture')
