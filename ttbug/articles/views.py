from django.shortcuts import render


# Create your views here.

def articles_list(request,block_id):
    block_id = int(block_id)
    return render(request,"articles_list.html")

def article_detail(request,article_id):
    article_id = int(article_id)
    pass

def article_create(request,block_id):
    block_id = int(block_id)
    pass
