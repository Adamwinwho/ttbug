from django.shortcuts import render
from .models import Blocks
# Create your views here.
from django.http import HttpResponse
from articles.models import Articles
from utils.paginator import paginate_queryset

def index(request):
    page_no = int(request.GET.get("page_no","1"))
    blocks = Blocks.objects.all().order_by("id")
    articles = Articles.objects.all().order_by("-id")
    articles_objs,pagination_data = paginate_queryset(articles,page_no)
    return render(request,"index.html",{"blocks":blocks,"articles":articles_objs,"pagination_data":pagination_data})
