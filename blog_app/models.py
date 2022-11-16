from email.policy import default
from turtle import title
from tinymce.models import HTMLField
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def user_posts(self):
        return self.author.all()

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    categories = models.ManyToManyField('Category')
    title = models.CharField(max_length=200)
    content = models.TextField()
    body = HTMLField()
    views = models.IntegerField(default=12, null=True)
    image = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    posted_on = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def post_image(self):
        try:
            return self.image.url
        except:
            return ""
    def get_absolute_url(self):
        return reverse('post', kwargs={
            'id':self.id
        })

    def __str__(self):
        return f"{self.author.user.username}'s post - {self.title}"

    def post_comment_count(self):
        comments = self.post.all()
        count = comments.count()
        return count

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    # parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.blog.title}"

    def total_comments(self):
        count = self.objects.all()
        return count
 
    