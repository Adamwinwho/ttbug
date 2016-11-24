from django.shortcuts import render
from .models import Blocks
# Create your views here.
from django.http import HttpResponse
from articles.models import Articles

def index(request):
    blocks = Blocks.objects.all().order_by("id")
    articles = Articles.objects.all().order_by("-id")
    return render(request,"index.html",{"blocks":blocks,"articles":articles})
