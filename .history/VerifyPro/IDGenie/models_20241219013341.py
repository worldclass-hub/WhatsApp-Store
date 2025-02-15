from django.db import models
from django.contrib.auth.models import User  # For author field
from django.utils import timezone
from ckeditor_5.fields import RichTextField

# BlogPost Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Use CKEditor for rich text input
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image
    video_url = models.URLField(blank=True, null=True)  # Optional video URL (for embedding)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post is last updated
    
    def __str__(self):
        return self.title

# BlogPostImage Model (for additional images)
class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_extra_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.blog_post.title}"

# Comment Model for blog posts
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # User who posted the comment
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp for when the comment is created
    
    def __str__(self):
        return f"Comment by {self.author} on {self.blog_post.title}"
