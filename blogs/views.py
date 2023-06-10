from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    hello_text = 'Hello world'
    return render(request, 'index.html', {'text':hello_text})