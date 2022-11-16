from django.urls import path, include
from .views import index, blog, post_detail, search

urlpatterns = [
    path("", index, name="index"),
    path("blog/", blog, name="blog"),
    # path("post/", post, name="post"),
    path("search/", search, name="search"),
    path("post/<id>/", post_detail, name="post"),
    
]