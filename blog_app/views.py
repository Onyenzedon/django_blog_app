from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.contrib.auth.models import User
from blog_app.models import Post, Comment, Author, Category
from blog_app.serializers import CommentSerializer, PostSerializer

# Create your views here.

def get_category_count():
    queryset = Post.objects.values("categories__title")
    print("Category count queryset: ", queryset)
    annot = queryset.annotate(Count('categories__title'))
    print("Annotated query: ", annot)
    return annot

def search(request):
    posts = Post.objects.all()
    q = request.GET.get("q")

    queryset = ""

    if q:
        queryset = posts.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
            ).distinct() # ensures return of non duplicate results.
    
   
    context = {
        'queryset': queryset
    }

    return render(request, "search_results.html", context)

def index(request):
    posts = Post.objects.all()
    
    print("Posts: ", posts)
    featured_posts = posts.filter(featured=True)

    context = {"posts":featured_posts}
    return render(request, "index.html", context)

def blog(request):
    category_count = get_category_count()
    posts = Post.objects.all().order_by("-id")
    paginator = Paginator(posts, 1)

    page_request = 'page'
    page = request.GET.get(page_request)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset  = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    latest_posts = posts[:3]
    context = {
        "posts":paginated_queryset,
        "paginated_queryset":paginated_queryset,
        "latest_posts":latest_posts,
        "page_request":page_request,
        "category_count" : category_count
    }
    return render(request, "blog.html", context)

# def post(request):
#     posts = Post.objects.get(id=)
#     comment = Comment.objects.filter(blog=post)
#     for post in posts:

#         post_comments = Comment.objects.filter(blog=post)

#     # post_serializers = PostSerializer(posts, many=True)
#     # comment_serializers = CommentSerializer(comments, many=True)

#     context = {
#         "posts":posts,
#         "comments":all_comments,
#         "post_comments":post_comments
#     }
#     return render(request, "post.html", context)

# @api_view(['GET'])
def post_detail(request, id):
    post = None
    try:
        post = Post.objects.get(id=id)
    except:
        print("Post with that ID doest not exist")

    post_comments = Comment.objects.filter(blog=post)    
    context = {
        "post":post,
        "comments": post_comments,
    }
    return render(request, "post.html", context)