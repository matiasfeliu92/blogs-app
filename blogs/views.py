import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Category, PostView
from blogs.forms import PostsForm

def index(request):
    hello_text = 'Hello world'
    # return render(request, 'index.html', {'text':hello_text})
    return JsonResponse({'message': hello_text})

def all_posts(request):
    # posts_data = list(Post.objects.all().values())
    posts_data = list(PostView.objects.all().values())
    print(posts_data)
    # return JsonResponse(posts_data, safe=False)
    return render(request, 'index.html', {'posts':posts_data})

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