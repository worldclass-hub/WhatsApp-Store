from django.contrib import admin
from .models import BlogPost, BlogParagraph, BlogPostImage
from .forms import BlogPostAdminForm


# Inline for additional paragraphs
class BlogParagraphInline(admin.TabularInline):
    model = BlogParagraph
    extra = 1  # Show 1 empty paragraph form by default

# Inline for additional images
class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1  # Show 1 empty image form by default


# BlogPost Admin
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

    # Use inlines for paragraphs and extra images
    inlines = [BlogParagraphInline, BlogPostImageInline]

    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'content', 'quote', 'image', 'video_url', 'author')
        }),
        ('Additional Options', {
            'fields': ('content_extra', 'image_extra', 'image_extra2', 'video_url_extra', 'quote_extra'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(BlogPost, BlogPostAdmin)
