from django.shortcuts import render
from blocks.views import Blocks
from .models import Articles

# Create your views here.

def articles_list(request,block_id):
    block_id = int(block_id)
    blocks = Blocks.objects.all()
    block = Blocks.objects.get(id=block_id)
    articles = Articles.objects.filter(block=block).order_by("-id")
    return render(request,"articles_list.html",{"blocks":blocks,"articles":articles})

def article_detail(request,article_id):
    article_id = int(article_id)
    pass

def article_create(request,block_id):
    block_id = int(block_id)
    pass
