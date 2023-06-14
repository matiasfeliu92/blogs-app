import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Post, Category
from blogs.forms import PostsForm

all_posts_query = """
        SELECT 
            blogs_post.id, 
            blogs_post.title, 
            blogs_post.content, 
            blogs_category.name as category_name, 
            blogs_post.pub_date, 
            blogs_post.image 
        FROM blogs_post 
        INNER JOIN blogs_category ON blogs_post.category_id = blogs_category.id
    """

def index(request):
    hello_text = 'Hello world'
    # return render(request, 'index.html', {'text':hello_text})
    return JsonResponse({'message': hello_text})

def all_posts(request):
    posts = Post.objects.raw(all_posts_query)
    return render(request, 'index.html', {'posts': posts})

def filter_posts(request):
    posts = Post.objects.raw(all_posts_query)
    if request.method == "POST":
        query = request.POST.get("findposts")
        print(query)
        posts_filtered = None
        if query:
            posts_filtered = Post.objects.filter(Q(category__name__icontains=query))
            if posts_filtered:
                return render(request, 'index.html', {'posts': posts_filtered})
            else:
                return render(request, 'index.html', {'notpost': 'not post found'})

    return render(request, 'index.html', {'posts': posts})


@csrf_exempt
def new_post(request):
    if request.method == 'POST':
        post_form = PostsForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
    else:
        post_form = PostsForm()
    
    return render(request, 'newPost.html', {'postForm': post_form})
