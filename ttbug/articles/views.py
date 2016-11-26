from django.shortcuts import render,redirect
from blocks.views import Blocks
from .models import Articles

# Create your views here.

def articles_list(request,block_id):
    block_id = int(block_id)
    blocks = Blocks.objects.all()
    block = Blocks.objects.get(id=block_id)
    articles = Articles.objects.filter(block=block).order_by("-id")
    return render(request,"articles_list.html",{"block_id":block_id,"blocks":blocks,"articles":articles})

def article_detail(request,article_id):
    article_id = int(article_id)
    article = Articles.objects.get(id=article_id)
    blocks = Blocks.objects.all()

    return render(request,"article_detail.html",{"block_id":article.block_id,"blocks":blocks,"article":article})

def article_create(request,block_id):
    block_id = int(block_id)
    blocks = Blocks.objects.all()
    if request.method == "GET":
        return render(request,"article_create.html",{"blocks":blocks,"block_id":block_id})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request,"article_create.html",{"blocks":blocks,"block_id":block_id,"error":"标题或内容不能为空","title":title,"content":content})
        if len(title)>100 or len(content)>10000:
            return render(request,"article_create.html",{"blocks":blocks,"block_id":block_id,"error":"标题或内容长度超过限制","title":title,"content":content})
        block = Blocks.objects.get(id=block_id)
        article = Articles(block=block,title=title,content=content)
        article.save()

        return redirect("/articles/list/%s" % block_id,{"blocks":blocks})
    
