import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Category
from blogs.forms import PostsForm

def index(request):
    hello_text = 'Hello world'
    # return render(request, 'index.html', {'text':hello_text})
    return JsonResponse({'message': hello_text})

def all_posts(request):
    posts_data = list(Post.objects.all().values())
    posts_page_title = 'Te invito los posts mas destacados'
    # return JsonResponse(posts_data, safe=False)
    return render(request, 'index.html', {'posts':posts_data, 'posts_page_title': posts_page_title})

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

@csrf_exempt
def new_category(request):
    if request.method == 'POST':
        cat_data = json.loads(request.body)
        print(cat_data)
        new_cat = Category(name=cat_data['name'])
        new_cat.save()
        return JsonResponse({'message': 'holaa'})