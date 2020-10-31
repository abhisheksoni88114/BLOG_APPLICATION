from django.db import models
from django.utils import timezone
from django.contrib.auth.models	import	User
from django.urls import reverse



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='draft', choices=[('published', 'Published'), ('draft', 'Draft')])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
class Comment(models.Model):
    name = models.CharField(max_length=40)
    com = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default='')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name